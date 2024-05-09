import peewee
from db import BaseModel

class Sales(BaseModel):
    name = peewee.CharField()