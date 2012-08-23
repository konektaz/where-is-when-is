Installation
============

First install requirements

```sh
pip install -r requirements.txt
```

Make sure you have postgis installed. Use version 1.5.3. Version 2 doesn't like Django. Once you install it, make sure you enable it on your database.

Clone the repository like this:

```sh
git clone https://github.com/konekta/where-is-when-is.git whereiswhenis && \
cd whereiswhenis
```

Copy settings file for your local machine like this:

```sh
cd konekta && cp settings.py local_settings.py && cd ..
```
Edit you local_settings.py and add your database login, password, host and port if needed.

Now set up the datebase:

```sh
python manage.py syncdb && \
python manage.py migrate
```

To load data use shell:

```
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
