from peewee import Model, PostgresqlDatabase
import os

db =  PostgresqlDatabase(database=os.environ.get('POSTGRES_DB'),
                                    user=os.environ.get('POSTGRES_USER'),
                                    password=os.environ.get('POSTGRES_PASSWORD'),
                                    host=os.environ.get('POSTGRES_HOST'))

class BaseModel(Model):
    class Meta:
       database = db
