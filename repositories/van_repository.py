from db.run_sql import run_sql

from models.van import Van
from models.customer import Customer


def select_all():
    vans = []
    sql = "SELECT * FROM vans"
    results = run_sql(sql)
    for result in results:
        van = Van(result['van_name'],result['reg_plate'],result['year'], result['capacity'],result['type'],result['id'])
        vans.append(van)
    return vans

def select(id):
    van = None 
    sql = "SELECT * FROM vans WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        van = Van(result['van_name'],result['reg_plate'],result['year'], result['capacity'],result['type'],result['id'])
    return van

def delete(id):
    sql = "DELETE FROM vans WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(van):
    sql = "UPDATE vans SET (van_name, reg_plate, year, capacity, type) = (%s, %s,%s,%s,%s) WHERE id = %s"
    values = [van.van_name, van.reg_plate, van.year, van.capacity, van.type, van.id]
    run_sql(sql, values)

def save(van):
    sql = "INSERT INTO vans (van_name, reg_plate, year, capacity, type) VALUES (%s,%s,%s,%s,%s) RETURNING id"
    values = [van.van_name, van.reg_plate, van.year, van.capacity, van.type]
    result = run_sql(sql, values)
    id = result[0]['id']
    van.id = id
