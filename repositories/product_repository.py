from db.run_sql import run_sql
# from models.manufacturer import Manufacturer
from models.product import Product

# import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

def save(product):
    #pseudo code:
    #check if there is a product category as same as the product
    #if not, run intert into and set stock_quantity to 1. for this category (stock_quantity) with a COUNT function
    #if yes, with the same count function, stock quantity + 1 , 
    # category = product.category #category from new product that i am adding
    # current_count = count(category)
    # new_stock = current_count
    
    # results = select_by_category(category)
    # if results.length >= 1:
    #     for row in results:
    #         sql = "UPDATE products SET (stock_quantity) = (%s) WHERE id = %s"
    #         values = [new_stock, row['id']]
    #         run_sql(sql, values)
    
    sql = "INSERT INTO products ( name, category, cost, selling_price, stock_quantity) VALUES ( %s, %s, %s, %s, %s ) RETURNING id"
    values = [product.name, product.category, product.cost, product.selling_price, product.stock_quantity]
    results = run_sql( sql, values )
    product.id = results[0]['id']
    return product

def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        #product = Product(row['name'], row['category'], row['cost'], row['selling_price'], row['id'])
        product = Product(row['name'], row['category'], row['cost'], row['selling_price'], row['stock_quantity'], row['id'])

        products.append(product)
    return products

def select_by_name(name):
    product = None

    sql = "SELECT * FROM products WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)[0]

    if result is not None:
        product = Product(result['name'], result['category'], result['cost'], result['selling_price'], result['stock_quantity'], result['id'])
        #product = Product(result['name'], result['category'], result['cost'], result['selling_price'], result['id'])

    return product

def select_by_category(category):
    product = None

    sql = "SELECT * FROM products WHERE category = %s"
    values = [category]
    result = run_sql(sql, values)

    # if result is not None:
    #     product = Product(result['name'], result['category'], result['cost'], result['selling_price'], result['stock_quantity'] , result['id'])
    #     #product = Product(result['name'], result['category'], result['cost'], result['selling_price'], result['id'])

    return result

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(name):
    sql = "DELETE FROM products WHERE name = %s"
    values = [name]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update_stock_quantity(product_id, new_stock):
    sql = "UPDATE products SET (stock_quantity) = (%s) WHERE id = %s"
    values = [new_stock, product_id]
    run_sql(sql, values)

def update(product):
    sql = "UPDATE products SET (name, category, cost, selling_price, stock_quantity) = (%s, %s, %s, %s, %s ) WHERE id = %s"
    values = [product.name, product.category, product.cost, product.selling_price, product.stock_quantity, product.id]
    run_sql(sql, values)

def count(category):
    sql = "SELECT COUNT (*) FROM products WHERE category = %s "
    values = [category]
    result = run_sql(sql, values)[0]
    return result