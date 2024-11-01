from models import User
from db import db
import peewee

class UserRepository:
    def create(self, user: User):
        try:
            db.create_tables([User])
            print("Tabela 'User' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'User' ja existe!")
        User.create(name=user.name, password=user.password)

    def list_all(self) -> list:
        query = User.select().execute()
        return query
