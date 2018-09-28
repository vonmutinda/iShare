# About iShare 
A Simple Minimalist image gallery by [von MUTINDA](https://fb.com/vonmutinda) . 

## Description & User Specifications
iShare is web application  that enable users to:

    1. view photos posted by von Mutinda
    3. Browse through various categories
    4. Search for photos
    5. Copy image link for sharing .

## Set-up and Installation

### Software Requirements
    - Python 3.6 *
    - PostgreSQL DMS
    - Text Editor ( preferably vscode / pyCharm )

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/vonmutinda/iShare && cd iShare`

Install [Postgres](https://www.postgresql.org/download/)
Install [Python](https://www.python.org/downloads/)

### Create a Virtual Environment
Run the following commands in the same terminal:
```sudo apt-get install python3.6-venv```
```python3.6 -m venv --without-pip virtual```
```curl https://bootstrap.pypa.io/get-pip.py | python```
```source virtual/bin/activate```

### Install Django Framework
``` bash
(virtual) pip install django==1.11 
```
confirm `django` is installed :
```bash
(virtual) python
>>> import django
>>> django.get_version()
>>> 1.11
>>>
```


### Database
Quickly create a database where your data is going to be persistent .
```
psql
you=#  CREATE DATABASE dbname;
```

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbname',
        'USER': 'your-username',
        'PASSWORD':'your-password'
    }
}
```

### Run Database Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### Running the app in development
In the same terminal type:
`python manage.py runserver` 

Open your browser on `http://localhost:8000/`, `http://127.0.0.1:8000`

## Technologies used
    - Python 3.7
    - Django 1.11
    - HTML
    - Bootstrap 4 
    - CSS 
    - Heroku
    - Postgresql

## Support and contact details
Contact me [von MUTINDA](maxwellmutinda@outlook.com) for any comments, reviews or insights .