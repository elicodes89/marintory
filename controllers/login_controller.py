# from flask import Flask, render_template, request, redirect
# from flask import Blueprint
# from models.user import User
# import repositories.login_repository as login_repository #create a save function here

# login_blueprint = Blueprint("login", __name__)


# @login_blueprint.route("/login", methods = ['POST'])
# def login():
#     name = request.form['name']
#     category = request.form['category']
#     user = User(name, category)
#     # user1 = User(name, category)
#     # user2 = User(name, category)
#     saved_user = login_repository.login(user)

#     return render_template("/login.html", user=saved_user)


# @users_blueprint.route("/users")
# def users():
#     users = user_repository.select_all()
#     return render_template("users/index.html", users = users)

# @users_blueprint.route("/users/login", methods = ['POST'])
# def login():
#     name = request.form['name']
#     category = request.form['category']
#     user = User(name, category)
#     # user1 = User(name, category)
#     # user2 = User(name, category)
#     saved_user = user_repository.save(user)

#     return render_template("/users/login.html", user=saved_user)

# @users_blueprint.route("/users/<id>")
# def show(id):
#     user = user_repository.select(id)
#     return render_template("users/index.html", user=user )
