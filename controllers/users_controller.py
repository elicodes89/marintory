from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository


users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/login")
def prelogin():
    # users = user_repository.select_all()
    # return render_template("users/index.html", users = users)
    return render_template("/users/index.html")

@users_blueprint.route("/inventory", methods = ['POST'])
def login():
    name = request.form['name']
    category = request.form['category']
    user = User(name, category)
    manufacturers = manufacturer_repository.select_all()
    products = product_repository.select_all()
    saved_user = user_repository.login(user)
    food_stock = product_repository.count('Food')[0] #i am using brackets as the sql count is returning an array and I do not want to see the brackets
    live_stock = product_repository.count('Live Stock')[0]
    accesories_stock = product_repository.count('Accesories')[0]
    food_stock_level = display_conditional_coloring(food_stock)
    live_stock_level = display_conditional_coloring(live_stock)
    accesories_stock_level = display_conditional_coloring(accesories_stock)

    return render_template("/inventory/index.html", user=saved_user, manufacturers = manufacturers, products = products, 
    food_stock = food_stock, live_stock = live_stock, accesories_stock = accesories_stock, 
    food_stock_level = food_stock_level, live_stock_level = live_stock_level, accesories_stock_level = accesories_stock_level )

@users_blueprint.route("/users/<id>")
def show(id):
    user = user_repository.select(id)
    return render_template("users/index.html", user=user )

def display_conditional_coloring(stock): #this is a local function
    if stock == 0:
        return "out_stock" #now we put this on html
    elif stock >= 1 and stock <= 5:
        return "low_stock"
    else:
        return "high_stock"

