This is the demo of our suggesting store market. This is the implementation of specific parts of our analysis based on RUP software development methodology. In the following the instruction for running codes is given.

# Requirements
This demo is done via using python3.7, django2.2 and we assume we are using Ubuntu18.04.. First we create a virtual environment.
```
virtualenv -p python3.7 venv
```
* Note that in order to run the above command we need to have both virtualenv and python3.7 installed on out system. We assume we are using Ubuntu18.04.

Then we activate our virtual environment and install requirements.  
```
source /venv/bin/activate
pip install -r requirements.txt
```


## Postgre Database configuration
In this demo we used postgresql. Use the following commands in order to create required role and database.
If you do not have postgresql installed here is good [link](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) to install it.
* Although mentioned link is for Ubuntu14.04 but it works fine for Ubuntu18.4.

```
CREATE DATABASE market;
CREATE USER admin WITH PASSWORD 'pass';

ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE market TO admin;
```
After that we installed and create database, the configuration is done in settings.py file for specified database, user and password.


## Run 
Now we are ready to run the code. First let's create our tables
```
python manage.py makemigrations
python manage.py migrate
```
To run the project
```
python manage.py runserver
```

### Icons and images
Most of the images for background and icons are used from [toptal](https://www.toptal.com/designers/subtlepatterns/), [flaticon](https://www.flaticon.com/) and fontawesome.