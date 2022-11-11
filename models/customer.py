class Customer:
    def __init__(self,customer_name, license, budget, friends, id=None):
        self.customer_name = customer_name
        self.license = license
        self.budget = budget
        self.friends = friends
        self.id = id