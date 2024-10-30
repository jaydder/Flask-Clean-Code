from peewee import PostgresqlDatabase, Model
import os


class BaseModel(Model):
    class Meta:
       database = PostgresqlDatabase('user',
                                    user=os.environ.get('POSTGRES_USER'),
                                    password=os.environ.get('POSTGRES_PASSWORD'),
                                    host=os.environ.get('POSTGRES_HOST'))
