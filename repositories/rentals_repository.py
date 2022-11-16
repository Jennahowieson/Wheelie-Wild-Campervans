import repositories.customer_repository as customer_repository
import repositories.van_repository as van_repository
from db.run_sql import run_sql
from models.customer import Customer
from models.rental import Rental
from models.van import Van
from datetime import date
import pdb 


def select_all():
    rentals = []
    sql = "SELECT * FROM rentals"
    results = run_sql(sql)
    for result in results:
        customer = customer_repository.select(result["customer_id"])
        van = van_repository.select(result["van_id"])
        rental = Rental(customer, van,result['start_date'], result['end_date'], result['id'])
        rentals.append(rental)
    return rentals

def select(id):
    rental = None 
    sql = "SELECT * FROM rentals WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        customer = customer_repository.select(result["customer_id"])
        van = van_repository.select(result["van_id"])
        rental = Rental(customer, van, result['start_date'], result['end_date'], result['id'])
    return rental

def delete(id):
    sql = "DELETE FROM rentals WHERE id = %s"
    values =[id]
    run_sql(sql, values)

def save(rental):
    sql = "INSERT INTO rentals (customer_id,van_id,start_date,end_date) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [rental.customer.id, rental.van.id, rental.start_date, rental.end_date]
    result = run_sql(sql, values)
    id = result[0]['id']
    rental.id = id

def update(rental):
    sql = "UPDATE rentals SET (customer_id,van_id,start_date,end_date) = (%s, %s,%s,%s) WHERE id = %s"
    values = [rental.customer.id, rental.van.id, rental.start_date, rental.end_date, rental.id]
    return run_sql(sql, values)


def current_rentals ():
    booked = []
    sql = "SELECT * FROM rentals WHERE start_date < CURRENT_DATE AND end_date > CURRENT_DATE "
    results = run_sql(sql)
    for result in results:
        customer = customer_repository.select(result["customer_id"])
        van = van_repository.select(result["van_id"])
        rental = Rental(customer, van,result['start_date'], result['end_date'], result['id'])
        booked.append(rental)
    return booked
    
    
    return run_sql(sql)

    rental = select(id)

    today = date.today()        
    start = rental.start_date
    end = rental.end_date
    booked_vans = []
    for van in vans:
        if start < today < end:
            booked_vans.append(van)
        return booked_vans 