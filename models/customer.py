from datetime import date, datetime
import pdb

import repositories.van_repository as van_repository
import repositories.customer_repository as customer_repository

class Customer:
    def __init__(self,customer_name, license, budget, friends, id=None):
        self.customer_name = customer_name
        self.license = license
        self.budget = budget
        self.friends = friends
        self.id = id
    
    def customer_type (self):
        customers = customer_repository.select_all()
        for customer in customers:
            if self.budget >=1000:
                customer_type = "Luxury"
            else:
                customer_type = "Budget"
        return customer_type

    def give_rental_options(self):
        available_vans = []
        customer_type = self.customer_type()
        vans = van_repository.select_by_type(customer_type)
        for van in vans:
            if self.friends < van.capacity:
                available_vans.append(van)
        return (available_vans)

    def len_rental_options(self):
        options = self.give_rental_options()
        return len(options)