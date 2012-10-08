# -*- coding: utf-8 -*-

from fabric.api import require, run, local, env, put, cd
from fabric.contrib.files import exists


env.use_ssh_config = True


# ------------------------- SITE DEFINITIONS -------------------------

def live():
    """
    Define the host for main site.
    """
    env.hosts = ['webdeploy@konekta']
    env.sitename = 'india.konekta.info'
    env.path = 'sites/%s' % (env.sitename,)
    env.repo = 'git://github.com/konekta/where-is-when-is.git'


# ------------------------- HELPER FUNCTIONS -------------------------

def _install_dependencies():
    """Use pip to install required packages."""
    # PyPI mirror list is at http://pypi.python.org/mirrors
    require('hosts', provided_by=[live])
    run('./%(path)s/env/bin/pip install --timeout=60 '
        '--log %(path)s/log/pip.log '
        '--download-cache PIP-DOWNLOAD-CACHE -M '
        '--mirrors b.pypi.python.org '
        '--mirrors c.pypi.python.org '
        '--mirrors d.pypi.python.org '
        '--mirrors e.pypi.python.org '
        '--mirrors f.pypi.python.org '
        '-r %(path)s/repo/requirements.txt 2>%(path)s/log/pip.errs' % env)


def _pull():
    """Pull the lastest version."""
    require('hosts', provided_by=[live])
    with cd('%(path)s/repo' % env):
        run('git pull origin master')

def _migrate():
    """Do the DB migrations"""
    require('hosts', provided_by=[live])
    run('./%(path)s/env/bin/python ./%(path)s/repo/manage.py migrate' % env)


def _upload_static_files():
    """Tell Django to (locally) collect all needed static files and upload
    and unpack them."""
    require('hosts', provided_by=[live])
    local("python manage.py collectstatic --noinput")
    #local("cd fluidinfo && python manage.py compress --force")
    local('tar cfj static.tar.bz2 static' % env)
    put('static.tar.bz2', '%(path)s/repo' % env)
    run('cd %(path)s/repo && '
        'tar xfj static.tar.bz2 && '
        'rm -f static.tar.bz2' % env)
    local('rm -rf static static.tar.bz2')


def _deploy():
    """Deploy the website."""
    _pull()
    _install_dependencies()
    _migrate()
    _upload_static_files()


# ------------------------- TOP-LEVEL COMMANDS -------------------------


def bootstrap():
    """Bootstrap the project"""
    require('hosts', provided_by=[live])

    run('mkdir -p %s/log' % env.path)

    if not exists(env.path + '/env'):
        run('virtualenv %s/env' % env.path)
    run('%s/env/bin/pip install -U pip' % env.path)
    run('%s/env/bin/pip install -U gunicorn gevent greenlet setproctitle'
        % env.path)

    run('git clone %s %s/repo' % (env.repo, env.path))


def push():
    _pull()


def deploy():
    """
    Wraps all the steps up to deploy to the live server.
    """
    _deploy()
