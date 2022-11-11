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


