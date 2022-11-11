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
