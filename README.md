Konekta web service
===================

Geolocate health services and make them available through a mobile site.


Installation
------------

You can quickly and easily setup a working Konektaz environment using Vagrant, VirtualBox and Fabric.
This repository contains the necessary Vagrantfile and fabfile, so you need to do is install
the necessary software.

#### Download and install VirtualBox:
You may wish to use a different provider. See the [Vagrant Docs](http://docs.vagrantup.com/v2/providers/index.html)
for more information.

[VirtualBox Downloads](https://www.virtualbox.org/wiki/Downloads)


#### Download and install Vagrant:
[Download Vagrant](http://downloads.vagrantup.com)


#### Clone the repository and cd into the repo:

```sh
git clone https://github.com/konekta/where-is-when-is.git whereiswhenis && \
cd whereiswhenis
```

#### Create and activate new virtual environment

```sh
virtualenv venv
venv/bin/activate
```

#### Install fabgis
Will also install Fabric and fabtools

```sh
pip install fabgis
```

#### Start your Vagrant box:
Our Vagrant file will download an Ubuntu 12.04LTS box to your system (unless it
already exists). This download will take quite some time! Once you have downloaded
the box, you will not have to download it again (for any future Vagrant projects which
require Ubuntu 12.04LTS)

```sh
vagrant up
```

After the download is complete, you will be asked which network interface you wish
Vagrant to bridge to; select the one which connects your host machine to the internet.


#### Deploy Konektaz to Vagrant
At this point, you must have installed VirtualBox and Vagrant on your host machine. You
must also have setup a virtualenvironment (called "venv") in the root dir of your Konektaz
clone. In that venv, you must have installed fabgis (and fabric and fabtools). Your
Vagrant instance must be running.

Now:

```sh
fab vagrant deploy
```

This will update the Ubuntu installation, download and install all the necessary system
requirements, clone the Konektaz repo, setup the databse, setup Apache and install
all venv requirements.


#### Connect!
You should now be able to connect to your local Konektaz instance. The simplest way is to
connect via apache by calling the Vagrant machine's LAN IP in your browser.
