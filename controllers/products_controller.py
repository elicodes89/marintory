from controllers.users_controller import redirect_to_inventory
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

products_blueprint = Blueprint("products", __name__)
users_blueprint = Blueprint("users", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products)

@products_blueprint.route("/products/<id>/update", methods = ['GET'])
def load_update_form(id):
    products = product_repository.select_all()
    return render_template("products/update.html", products = products, id = id)

@products_blueprint.route("/products/productname/<name>")
def show_by_name(name):
    product = product_repository.select_by_name(name)
    return render_template("products/show_name.html", product = product)

@products_blueprint.route("/products/productcategory/<category>")
def show_by_category(category):
    product = product_repository.select_by_category(category)
    return render_template("products/show_category.html", product = product)

@products_blueprint.route("/products", methods = ['POST'])
def add_new_product():
    name = request.form['name']
    category = request.form['category']
    cost = request.form['cost']
    selling_price = request.form['selling_price']

    #gets the current count based on category of the new product to add
    current_count = product_repository.count(category)[0]

    #sets new_stock to latest value
    new_stock = current_count + 1
    
    #gets all records from product table based on category 
    results = product_repository.select_by_category(category)

    #if there is at least one existing product based on category, 
    # update the stock_quantity of each record
    if len(results) >= 1:
        for row in results:
            product_id = row['id']
            product_repository.update_stock_quantity(new_stock, product_id)

    #Add new product with the new_stock
    product = Product(name, category, cost, selling_price, new_stock) #product instance    
    product_repository.save(product)    

    return redirect ("/products")    

@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_to_delete = product_repository.select_by_id(id)
    category = product_to_delete.category
    current_count = product_repository.count(category)[0]
    new_stock = current_count - 1

    results = product_repository.select_by_category(category)
    if len(results) >= 1:
        for row in results:
            product_id = row['id']
            product_repository.update_stock_quantity(new_stock, product_id)
    
    product_repository.delete_by_id(id)
    return redirect('/products')

# @products_blueprint.route("/products/<id>/update" , methods=['GET'])
# def update_product(id):
#     product = product_repository.update(id)
#     manufacturer = manufacturer_repository.select_all()
#     return render_template ("products/index.html" , product = product, manufacturer = manufacturer)

@products_blueprint.route("/products/<id>/update" , methods=['POST'])
def update_product(id):
    name = request.form['name']
    category = request.form['category']
    cost = request.form['cost']
    selling_price = request.form['selling_price']
    stock_quantity = product_repository.count(category)[0] #0 to not get an array, just the actual value. remember this
    product = Product(name, category, cost, selling_price, stock_quantity, id) #product instance    
    
    product_repository.update(product)

    return redirect ("/products")
  

