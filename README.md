# CRUD Multi Layered

This project has created to study multi layers in python using *docker* to up server web flask and database *postgres*.

this application use .env file to security.

## Variables Enviroment

- SECRET_KEY        : hash or passphrase to wtforms
- FLASK_DEBUG       : debug level flask
- FLASK_APP         : path containing application 
- POSTGRES_DB       : name database
- POSTGRES_USER     : user to login database
- POSTGRES_PASSWORD : password to login database
- POSTGRES_HOST     : IP host from database 

## Endpoints


`POST /`

    register new user , using fields "name"  and "password"

`GET /list_user`
    
    List all User registed in database

`POST /list_user`
    
    Delete user seleted with index

`POST /update`

    Update dates from user created, pass "old_name", "new_name" and "new_password"


## Address from services

- flask/web: 10.5.0.4 
- postgres/database: 10.5.0.5

## Run the app

    docker compose up