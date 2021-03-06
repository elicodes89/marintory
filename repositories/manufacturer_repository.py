from db.run_sql import run_sql
from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manufacturer_repository


def save(manufacturer):
    sql = "INSERT INTO manufacturers ( name, email, contact_number, category) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [manufacturer.name, manufacturer.email, manufacturer.contact_number, manufacturer.category]
    results = run_sql( sql, values )
    manufacturer.id = results[0]['id']
    return manufacturer

def select_all():
    manufacturers = []
    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)
    for row in results:
        manufacturer = Manufacturer(row['name'], row['email'], row['contact_number'], row['category'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers

def select_by_name(name):
    manufacturer = None

    sql = "SELECT * FROM manufacturers WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'], result['email'], result['contact_number'], result['category'], result['id'])

    return manufacturer

def select_by_id(id):
    manufacturer = None

    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'], result['email'], result['contact_number'], result['category'], result['id'])

    return manufacturer

def select_by_category(category):
    manufacturer = None

    sql = "SELECT * FROM manufacturers WHERE category = %s"
    values = [category]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'], result['email'], result['contact_number'], result['category'], result['id'])
        return manufacturer

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete_by_id(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete(name):
    sql = "DELETE FROM manufacturers WHERE name = %s"
    values = [name]
    run_sql(sql, values)

def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, email, contact_number, category) = (%s, %s, %s, %s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.email, manufacturer.contact_number, manufacturer.category, manufacturer.id]
    run_sql(sql, values)



