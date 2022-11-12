class Rental:
    def __init__(self,customer,van,start_date,end_date,id=None):
        self.customer = customer
        self.van = van
        self.start_date = start_date
        self.end_date = end_date
        self.id = id
        