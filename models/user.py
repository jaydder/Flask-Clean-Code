import peewee
from db import BaseModel, db

class User(BaseModel):
    name = peewee.CharField()
    password = peewee.CharField()
