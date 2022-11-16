from db.run_sql import run_sql
import pdb
from models.van import Van
import repositories.rentals_repository as rentals_repository

def select_all():
    vans = []
    sql = "SELECT * FROM vans"
    results = run_sql(sql)
    for result in results:
        van = Van(result['van_name'],result['reg_plate'],result['year'], result['capacity'],result['type'],result['id'])
        vans.append(van)
    vans.sort(key=lambda x: x.van_name)
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

def select_by_type(type):
    vans = []
    sql = "SELECT * FROM vans WHERE type = %s"
    values= [type]
    results =  run_sql(sql, values)
    for result in results:
        van = Van(result['van_name'],result['reg_plate'],result['year'], result['capacity'],result['type'],result['id'])
        vans.append(van)
    vans.sort(key=lambda x: x.van_name)
    return vans

def currently_in_use ():
    in_use = []
    current_rentals = rentals_repository.current_rentals()
    van_ids = [van.id for van in current_rentals]
    all_vans = select_all()
    for van in all_vans:
        if van.id in van_ids:
            in_use.append(van)
    return in_use


