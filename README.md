# Sample Django app

Experimenting with Django, Test automation with Python and CI.

## Commands 

Generate Django project

```bash
$ django-admin startproject damian
```
Create an app

```bash
$ python3 manage.py createapp hello
```
Run app in test server

```bash
$ python3 manage.py runserver
```

Database Migration
```bash
$ python3 manage.py makemigrations hello
No changes detected in app 'hello'
$ python3 manage.py migrate hello
Operations to perform:
  Apply all migrations: hello
Running migrations:
  Applying hello.0001_initial... OK
  Applying hello.0002_auto_20200511_1504... OK
```

Interact Python Shell (for example to manipulate data in database)
```bash
$ python3 manage.py shell
```

## Testing

- Backend: Database models
- Frontend: views
- E2E - Selenium


## CI

- generate requirements file

```python
$ pip3 freeze >> requirements.txt
```
- create travis config `.travis.yaml` Example:

```python
language: python
python: 3.6
install: pip install -r requirements.txt
script: python manage.py test 
```


## License
[MIT](https://choosealicense.com/licenses/mit/)