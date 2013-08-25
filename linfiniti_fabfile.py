#!/bin/python
# ~/fabfile.py
# A Fabric file for carrying out various administrative tasks.
# Tim Sutton, Jan 2013

# To use this script make sure you have fabric and fabtools.
# pip install fabric fabtools

import os
from fabric.api import *
from fabric.contrib.files import contains, exists, append, sed
import fabtools
from fabgis import postgres, common
# Don't remove even though its unused
from fabtools.vagrant import vagrant

# Usage fab localhost [command]
#    or fab remote [command]
#  e.g. fab localhost update

# This will get replaced in various places, for a generic site, it may be
# all you need to change...
PROJECT_NAME = 'konektaz'
#env.user = 'vagrant'


def _all():
    """Things to do regardless of whether command is local or remote."""

    # Key is hostname as it resolves by running hostname directly on the server
    # value is desired web site url to publish the repo as.

    with hide('output'):
        env.user = run('whoami')
        env.hostname = run('hostname')
        env.repo_site_name = 'konektaz'
        # where to check the repo out to
        env.webdir = '/home/web'
        # repo uri
        env.git_url = 'https://github.com/timlinux/where-is-when-is.git'
        # checkout name for repo
        env.repo_alias = PROJECT_NAME
        # user wsgi should run as (will be created if needed)
        env.wsgi_user = 'vagrant'
        # Deploy dir - e.g. /home/web/foo
        env.code_path = os.path.join(env.webdir, env.repo_alias)
        show_environment()

###############################################################################
# Next section contains helper methods tasks
###############################################################################


@task
def rsync_local():
    _all()
    with cd('/home/web/'):
        run('rsync -va /vagrant/ %s/ --exclude \'venv\'' % PROJECT_NAME)
    collect_static()


@task
def collect_static():
    _all()
    with cd('%s' % env.code_path):
        run('venv/bin/python manage.py collectstatic --noinput')
        wsgi_file = 'konekta/wsgi.py'
        sudo('find . -iname \'*.pyc\' -exec rm {} \;')
        run('touch %s' % wsgi_file)


def replace_tokens(conf_file):
    if '.templ' == conf_file[-6:]:
        conf_file = conf_file.replace('.templ', '')

    run(
        'cp %(conf_file)s.templ %(conf_file)s' % {
            'conf_file': conf_file})
    # We need to replace these 3 things in the conf file:
    # [SERVERNAME] - web site base url e.g. foo.com
    # [ESCAPEDSERVERNAME] - the site base url with escaping e.g. foo\.com
    # [SITEBASE] - dir under which the site is deployed e.g. /home/web
    # [SITENAME] - should match env.repo_alias
    # [SITEUSER] - user apache wsgi process should run as
    # [CODEBASE] - concatenation of site base and site name e.g. /home/web/app
    escaped_name = env.repo_site_name.replace('.', '\\\.')
    fastprint('Escaped server name: %s' % escaped_name)
    sed('%s' % conf_file, '\[SERVERNAME\]', env.repo_site_name)
    sed('%s' % conf_file, '\[ESCAPEDSERVERNAME\]', escaped_name)
    sed('%s' % conf_file, '\[SITEBASE\]', env.webdir)
    sed('%s' % conf_file, '\[SITENAME\]', env.repo_alias)
    sed('%s' % conf_file, '\[SITEUSER\]', env.wsgi_user)
    sed('%s' % conf_file, '\[CODEBASE\]', env.code_path)


def setup_website():
    """Initialise or update the git clone.

    e.g. to update the server

    fab -H 1.1.1.1:111 remote setup_website

    or if you have configured env.hosts, simply

    fab remote setup_website
    """

    fabtools.require.postfix.server(env.repo_alias)
    fabtools.require.deb.package('libapache2-mod-wsgi')
    # Find out if the wsgi user exists and create it if needed e.g.
    fabtools.require.user(
        env.wsgi_user,
        create_group=env.wsgi_user,
        system=True,
        comment='System user for running the wsgi process under')

    if not exists(env.webdir):
        sudo('mkdir -p %s' % env.plugin_repo_path)
        sudo('chown %s.%s %s' % (env.user, env.user, env.webdir))

    # Clone and replace tokens in apache conf

    conf_file = (
        '%s/apache/%s.apache.conf' % (
            env.code_path, env.repo_alias))

    run(
        'cp %(conf_file)s.templ %(conf_file)s' % {
            'conf_file': conf_file})

    replace_tokens(conf_file)

    with cd('/etc/apache2/sites-available/'):
        if exists('%s.apache.conf' % env.repo_alias):
            sudo('a2dissite %s.apache.conf' % env.repo_alias)
            fastprint('Removing old apache2 conf', False)
            sudo('rm %s.apache.conf' % env.repo_alias)

        sudo('ln -s %s .' % conf_file)

    # wsgi user needs pg access to the db
    postgres.require_postgres_user(env.wsgi_user, env.wsgi_user)
    postgres.require_postgres_user('timlinux', 'timlinux')
    postgres.require_postgres_user('readonly', 'readonly')
    postgres.create_postgis_1_5_db('%s' % PROJECT_NAME, env.wsgi_user)
    grant_sql = 'grant all on schema public to %s;' % env.wsgi_user
    # assumption is env.repo_alias is also database name
    run('psql %s -c "%s"' % (env.repo_alias, grant_sql))
    grant_sql = (
        'GRANT ALL ON ALL TABLES IN schema public to %s;' % env.wsgi_user)
    # assumption is env.repo_alias is also database name
    run('psql %s -c "%s"' % (env.repo_alias, grant_sql))
    grant_sql = (
        'GRANT ALL ON ALL SEQUENCES IN schema public to %s;' % env.wsgi_user)
    run('psql %s -c "%s"' % (env.repo_alias, grant_sql))
    pwd_sql = 'ALTER USER timlinux WITH PASSWORD \'timlinux\';'
    pwd_sql = 'ALTER USER %s WITH PASSWORD \'%s\';' % (
        env.wsgi_user, env.wsgi_user)
    run('psql %s -c "%s"' % (env.repo_alias, pwd_sql))
    #with cd(env.code_path):
    # run the script to create the sites view
    #run('psql -f sql/3-site-view.sql %s' % env.repo_alias)

    # Add a hosts entry for local testing - only really useful for localhost
    hosts = '/etc/hosts'
    if not contains(hosts, env.repo_site_name):
        append(hosts, '127.0.0.1 %s' % env.repo_site_name, use_sudo=True)
    if not contains(hosts, 'www.' + env.repo_site_name):
        append(hosts,
               '127.0.0.1 %s' % 'www.' + env.repo_site_name,
               use_sudo=True)
        # Make sure mod rewrite is enabled
    sudo('a2enmod rewrite')
    # Enable the vhost configuration
    sudo('a2ensite %s.apache.conf' % env.repo_alias)

    # Check if apache configs are ok - script will abort if not ok
    sudo('/usr/sbin/apache2ctl configtest')
    sudo('a2dissite default')
    fabtools.require.service.restarted('apache2')

    #Setup a writable media dir for apache
    media_path = '%s/media' % env.code_path
    if not exists(media_path):
        sudo('mkdir %s' % media_path)
        sudo('chown %s.%s %s' % (env.wsgi_user, env.wsgi_user, env.code_path))


def setup_venv():
    """Initialise or update the virtual environmnet.


    To run e.g.::

        fab -H 1.1.1.1:111 remote setup_venv

    or if you have configured env.hosts, simply

        fab remote setup_venv
    """

    with cd(env.code_path):
        # Ensure we have a venv set up
        fabtools.require.python.virtualenv('venv')

    # Gdal does not build cleanly from requirements so we follow advice
    # from http://ubuntuforums.org/showthread.php?t=1769445
    pip_path = os.path.join(env.code_path, 'venv', 'bin', 'pip')
    gdal_build_path = os.path.join(env.code_path, 'venv', 'build', 'GDAL')

    result = run('%s install --no-install GDAL' % pip_path)
    if 'Requirement already satisfied ' not in result:
        with cd(gdal_build_path):
            run('python setup.py build_ext --include-dirs=/usr/include/gdal')
            run('%s install --no-download GDAL' % pip_path)

    with cd(env.code_path):
        run('venv/bin/pip install -r requirements.txt')


@task
def update_git_checkout(branch='master'):
    """Make sure there is a read only git checkout.

    Args:
        branch: str - a string representing the name of the branch to build
            from. Defaults to 'master'

    To run e.g.::

        fab -H 1.1.1.1:111 remote update_git_checkout

    or if you have configured env.hosts, simply

        fab remote update_git_checkout

    """
    _all()
    fabtools.require.deb.package('git')
    if not exists(env.code_path):
        fastprint('Repo checkout does not exist, creating.')
        user = run('whoami')
        sudo('sudo mkdir -p %s' % env.webdir)
        sudo('chown %s.%s %s' % (user, user, env.webdir))
        with cd(env.webdir):
            run('git clone %s %s' % (env.git_url, env.repo_alias))
    else:
        fastprint('Repo checkout does exist, updating.')
        with cd(env.code_path):
            # Get any updates first
            run('git fetch')
            # Get rid of any local changes
            run('git reset --hard')
            # Get back onto master branch
            run('git checkout master')
            # Remove any local changes in master
            run('git reset --hard')
            # Delete all local branches
            run('git branch | grep -v \* | xargs git branch -D')

    with cd(env.code_path):
        if branch != 'master':
            run('git branch --track %s origin/%s' % (branch, branch))
            run('git checkout %s' % branch)
        else:
            run('git checkout master')
        run('git pull')
        #run('./runcollectstatic.sh')
        wsgi_file = 'konekta/wsgi.py'
        run('touch %s' % wsgi_file)

###############################################################################
# Next section contains actual tasks
###############################################################################


@task
def get_dump():
    """Get a dump of the database from the server."""
    _all()
    postgres.get_postgres_dump(env.repo_alias, ignore_permissions=True)


@task
def restore_dump(file_name=None, migrations=False):
    """Upload dump to host, remove existing db, recreate then restore dump."""
    _all()
    postgres.restore_postgres_dump(
        env.repo_alias,
        ignore_permissions=True,
        file_name=file_name,
        user=env.wsgi_user,
        password=env.wsgi_user)


@task
def deploy(branch='master'):
    """Do a fresh deployment of the site to a server.

    Args:
        branch: str - a string representing the name of the branch to build
            from. Defaults to 'master'.

    To run e.g.::

        fab -H 1.1.1.1:111 remote deploy

        or to package up a specific branch (in this case v1)

        fab -H 1.1.1.1:111 remote deploy:v1

    For live server:

        fab -H 1.1.1.1:111 remote deploy

    or if you have configured env.hosts, simply

        fab remote deploy
    """

    common.add_ubuntugis_ppa()
    ## fabgis.setup_postgis()
    postgres.setup_postgis_1_5()
    fabtools.require.deb.package('subversion')
    fabtools.require.deb.package('python-pip')
    fabtools.require.deb.package('libxml2-dev')
    fabtools.require.deb.package('libxslt1-dev')
    fabtools.require.deb.package('python-dev')
    fabtools.require.deb.package('build-essential')
    fabtools.require.deb.package('libgdal1-dev')
    fabtools.require.deb.package('gdal-bin')
    update_git_checkout(branch)
    setup_venv()
    setup_website()
    collect_static()


@task
def show_environment():
    """For diagnostics - show any pertinent info about server."""
    fastprint('\n-------------------------------------------------\n')
    fastprint('User: %s\n' % env.user)
    fastprint('Host: %s\n' % env.hostname)
    fastprint('Site Name: %s\n' % env.repo_site_name)
    fastprint('Dest Path: %s\n' % env.webdir)
    fastprint('Wsgi User: %s\n' % env.wsgi_user)
    fastprint('Git Url: %s\n' % env.git_url)
    fastprint('Repo Alias: %s\n' % env.repo_alias)
    fastprint('-------------------------------------------------\n')
