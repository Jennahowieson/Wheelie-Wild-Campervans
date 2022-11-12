from db.run_sql import run_sql

from models.van import Van
from models.customer import Customer

def select_all():
    customers = []
    sql = "SELECT * FROM customers"
    results = run_sql(sql)
    for result in results:
        customer = Customer(result['customer_name'],result['license'],result['budget'], result['friends'],result['id'])
        customers.append(customer)
    return customers

def select(id):
    customer = None 
    sql = "SELECT * FROM customers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        customer = Customer(result['customer_name'],result['license'],result['budget'], result['friends'],result['id'])
    return customer

def delete(id):
    sql = "DELETE FROM customers WHERE id = %s"
    values =[id]
    run_sql(sql, values)

def update(customer):
    sql = "UPDATE customers SET (customer_name, license, budget, friends) = (%s, %s,%s,%s) WHERE id = %s"
    values = [customer.customer_name, customer.license, customer.budget, customer.friends, customer.id]
    run_sql(sql, values)

def save(customer):
    sql = "INSERT INTO customers (customer_name, license, budget, friends) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [customer.customer_name, customer.license, customer.budget, customer.friends]
    result = run_sql(sql, values)
    id = result[0]['id']
    customer.id = id
