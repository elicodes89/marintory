from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer    
import repositories.manufacturer_repository as manufacturer_repository

users_blueprint = Blueprint("manufacturers", __name__)

@users_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers = manufacturers)