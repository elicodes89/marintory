from db.run_sql import run_sql
# from models.manufacturer import Manufacturer
from models.product import Product

# import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

def save(product):
    sql = "INSERT INTO products ( name, category, cost, selling_price) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [product.name, product.category, product.cost, product.selling_price]
    results = run_sql( sql, values )
    product.id = results[0]['id']
    return product

def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        product = Product(row['name'], row['category'], row['cost'], row['selling_price'], row['id'])
        products.append(product)
    return products

def select_by_name(name):
    product = None

    sql = "SELECT * FROM products WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)[0]

    if result is not None:
        product = Product(result['name'], result['category'], result['cost'], result['selling_price'], result['id'])

    return product

def select_by_category(category):
    product = None

    sql = "SELECT * FROM products WHERE category = %s"
    values = [category]
    result = run_sql(sql, values)[0]

    if result is not None:
        product = Product(result['name'], result['category'], result['cost'], result['selling_price'], result['id'])

    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(name):
    sql = "DELETE FROM products WHERE name = %s"
    values = [name]
    run_sql(sql, values)

def update(product):
    sql = "UPDATE products SET (name, category, cost, selling_price) = (%s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.category, product.cost, product.selling_price, product.id]
    run_sql(sql, values)

def count(category):
    sql = "SELECT COUNT (*) FROM products WHERE category = %s "
    values = [category]
    result = run_sql(sql, values)[0]
    return result