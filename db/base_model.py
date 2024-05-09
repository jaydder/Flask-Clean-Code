import peewee

class BaseModel(peewee.Model):
    class Meta:
        database = peewee.SqliteDatabase('sales.db')