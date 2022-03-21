from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product

import repositories.product_repository as product_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products)

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
    product = Product(name, category, cost, selling_price)
    product_repository.save(product)
    product_repository.select_all()

    return redirect ("/products")

@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')
