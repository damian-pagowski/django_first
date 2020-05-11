1 create django project
    damian@laptop:~/Desktop/cs50/django/damian/damian$ django-admin startproject damian
- looks like project is just a container with bunch of utility/config files
- can hold one or many apps inside
- 
2 create django app
    damian@laptop:~/Desktop/cs50/django/damian$ python3 manage.py startapp hello


3 run

damian@laptop:~/Desktop/cs50/django/damian$ python3 manage.py runserver^C


4 database migrations


damian@laptop:~/Desktop/cs50/django/damian$ python3 manage.py makemigrations

5 apply migration file

damian@laptop:~/Desktop/cs50/django/damian$ python3 manage.py sqlmigrate hello 0001




