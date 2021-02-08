import sys
sys.path.append('.')

from flask import Flask, render_template, request, redirect
from src.controller.category_controller import CategoryController
from src.models.category_model import Category


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/listcategory')
def category():
    category = CategoryController().read_all()
    return render_template('listcategory.html', list=category)


@app.route('/category/update', methods=['POST'])
def update_category_post():
    controller = CategoryController()
    id = request.form.get('id')
    category = controller.read_by_id(int(id))
    category.name = request.form.get('name')
    category.description = request.form.get('description')
    controller.save(category)
    return redirect('/listcategory')      


@app.route('/category/update/<int:id>', methods=['GET'])
def update_category_get(id):
    category = CategoryController().read_by_id(int(id))
    return render_template('category.html', category=category, action = 'update')


@app.route('/category/create', methods=['POST', 'GET'])
def create_category():
    if request.method == 'POST':
        controller = CategoryController()
        name = request.form.get('name')
        description = request.form.get('description')
        category = Category(name, description)
        controller.save(category)
        return redirect('/listcategory')       
    return render_template('category.html', action = 'create')


@app.route('/category/delete/<int:id>')
def delete_category(id):
    category = CategoryController().read_by_id(id)
    CategoryController().delete(category)
    return redirect('/listcategory')


app.run(debug=True)
