from datetime import date


def date_in_words(date):
        day = date.strftime("%d")
        month = date.strftime("%B")
        year = date.strftime("%Y")
        return (day +" "+ month + " " + year)
        
date_in_words (2022-12-14)