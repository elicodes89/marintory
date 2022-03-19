from db.run_sql import run_sql
# from models.manufacturer import Manufacturer
from models.user import User
# from models.product import Product

import repositories.user_repository as user_repository

#create a user
def save(user):
    sql = "INSERT INTO users (name, category) VALUES (%s, %s) RETURNING *"
    values = [user.name, user.category]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

#delete all users
def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

#delete user by id/also tested delete by name
def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)



