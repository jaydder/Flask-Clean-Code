import peewee
from db import BaseModel, db

class User(BaseModel):
    id = peewee.AutoField()
    name = peewee.CharField()
    password = peewee.CharField()
