class Rental:
    def __init__(self,customer,van,start_date,end_date,id=None):
        self.customer = customer
        self.van = van
        self.start_date = start_date
        self.end_date = end_date
        self.id = id
    
    def end_date_in_words(self):
        day = self.end_date.strftime("%d")
        month = self.end_date.strftime("%B")
        year = self.end_date.strftime("%Y")
        return (day +" "+ month + " " + year)
    
    def start_date_in_words(self):
        day = self.start_date.strftime("%d")
        month = self.start_date.strftime("%B")
        year = self.start_date.strftime("%Y")
        return (day +" "+ month + " " + year)