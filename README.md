# [Instagram](https://instajboom.herokuapp.com)
#### Web clone of the Instagram app

#### By **[Jeff Musa](https://github.com/jeffmusa)**

## Description
This is a simple web clone of the instagram website. A user can create an account and sign into it. 
The site supports uploading images, and commenting on what other users have uploaded. 
users can view photos uploaded by other users in the home page of app.

## Specifications
Find the specs [here](https://github.com/DevWaweru/InstaBoom/blob/master/SPECS.md)

## Set Up and Installations

### Prerequisites
1. Ubuntu Software
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/jeffmusa/InstaBoom.git && cd InstaBoom`

### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE insta;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'insta'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
```
### Run initial Migration
```bash
python3.6 manage.py makemigrations gram
python3.6 manage.py migrate
```

### Run the app
```bash
python3.6 manage.py runserver
```
Open terminal on `localhost:8000`

## Known bugs
Like and Follow functionality does not work

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me on developer.waweru@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Jeff Musa**
