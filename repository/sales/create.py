from models import User
import peewee

class Create:
    def create(self, name=None, password=None):
        try:
            User.create_table()
            print("Tabela 'User' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'User' ja existe!")
        User.create(name=name, password=password)
