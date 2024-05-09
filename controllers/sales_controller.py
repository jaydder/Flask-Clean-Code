from .flask_context import app
from service.sales import Create

sales = Create()
class SalesController:

    @app.route('/', methods=['GET'])
    def index():
        sales.create('batata')
        return '<h1>Hellow</h1>'