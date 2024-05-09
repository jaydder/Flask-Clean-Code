from repository.sales import Create
class ServiceSales:
    sales = Create()

    def create(self, name):
        self.sales.create(name)