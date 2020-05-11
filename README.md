# Commands - generate and create app
## generate django project
- damian@laptop:~/Desktop/cs50/django/damian/damian$ django-admin startproject damian
- looks like project is just a container with bunch of utility/config files
- can hold one or many apps inside
- 
## geerate django app
    damian@laptop:~/Desktop/cs50/django/damian$ python3 manage.py startapp hello

## run

damian@laptop:~/Desktop/cs50/django/damian$ python3 manage.py runserver^C


# Database migration

## create migration file (schema snapshot?) & apply
damian@laptop:~/Desktop/cs50/django/damian$ python3 manage.py makemigrations hello
No changes detected in app 'hello'
damian@laptop:~/Desktop/cs50/django/damian$ python3 manage.py migrate hello
Operations to perform:
  Apply all migrations: hello
Running migrations:
  Applying hello.0001_initial... OK
  Applying hello.0002_auto_20200511_1504... OK

# python shell (interactive)

damian@laptop:~/Desktop/cs50/django/damian$ python3 manage.py shell

# Testing Web Applications with Django

## The Back-End (database models)

- unittest module
- django specific
- testing database modules (slq alchemy like orm)

## frontend (views)