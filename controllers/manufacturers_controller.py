from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer    

import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers = manufacturers)

@manufacturers_blueprint.route("/manufacturers/manufacturername/<name>")
def show_by_name(name):
    manufacturer = manufacturer_repository.select_by_name(name)
    return render_template("manufacturers/show_name.html", manufacturer = manufacturer)

@manufacturers_blueprint.route("/manufacturers/manufacturercategory/<category>")
def show_by_category(category):
    manufacturer = manufacturer_repository.select_by_category(category)
    return render_template("manufacturers/show_category.html", manufacturer = manufacturer)
