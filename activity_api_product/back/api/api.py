import sys
sys.path.append('.')

from flask import Flask
from flask_restful import Api
from back.controller.product_controller import ProductController

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductController, '/api/product', endpoint = 'products')
api.add_resource(ProductController, '/api/product/<int:id>', endpoint = 'product')

@app.route('/')
def index():
    return 'Hi'

app.run(debug=True)