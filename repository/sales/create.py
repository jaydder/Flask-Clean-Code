from models import Sales
import peewee

class Create:
    def create(self, name='batata'):
        try:
            Sales.create_table()
            print("Tabela 'Sales' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'Author' ja existe!")
        Sales.create(name=name)
