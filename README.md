Konekta web service
===================

Geolocate health services and make them available through a mobile site.


Installation
------------

First, clone the repository like this:

```sh
git clone https://github.com/konekta/where-is-when-is.git whereiswhenis && \
cd whereiswhenis
```

Create a new virtual environment

```sh
virtualenv env
. env/bin/activate
```

Then install requirements

```sh
pip install -r requirements.txt
```

Make sure you have postgis installed. Use version 1.5.3. Version 2 doesn't like
Django. Once you install it, make sure you enable it on your database.

Copy the sample local_settings file for your local machine like this:

```sh
cp konekta/local_settings.py.example konekta/local_settings.py
```

Edit your local_settings.py and add your database login, password, host and
port if needed.

Now set up the datebase:

```sh
python manage.py syncdb
python manage.py migrate
```

To load data use shell:

```sh
python manage.py shell
```

And then in that shell:

```python
from world import load
load.run()
# Ctrl+D to exit
```

And run your app:

```sh
python manage.py runserver 0.0.0.0:8000
```

Deployment

