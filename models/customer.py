from datetime import date, datetime

import repositories.van_repository as van_repository

class Customer:
    def __init__(self,customer_name, license, budget, friends, id=None):
        self.customer_name = customer_name
        self.license = license
        self.budget = budget
        self.friends = friends
        self.id = id

    def give_rental_options(self):
        available_vans = []
        vans = van_repository.select_all()
        for van in vans:
            if self.friends < van.capacity:
                available_vans.append(van.van_name)
        return (available_vans)
