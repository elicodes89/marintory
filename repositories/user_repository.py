from db.run_sql import run_sql
from models.user import User


#create a user
def login(user):
    sql = "INSERT INTO users (name, category) VALUES (%s, %s) RETURNING *"
    values = [user.name, user.category]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

#a for loop to select all users by name and id and append them into an empty list
def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['category'], row['id'])
        users.append(user)
    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User(result['name'], result['category'], result['id'] )
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



