Installation
============

First install requirements

```sh
pip install -r requirements.txt
```

Make sure you have postgis installed. Use version 1.5.3. Version 2 doesn't like Django. Once you install it, make sure you enable it on your database.

Go to the folder you've check out the repository and:

```sh
python manage.py syncdb && \
python manage.py migrate && \
python manage.py runserver 0.0.0.0:8000
```

To load data use shell:

```
python manage.py shell
```

And then in that shell:

```python
from world import load
load.run()
```
