from datetime import date
import repositories.van_repository as van_repository
import repositories.customer_repository as customer_repository
import repositories.rentals_repository as rentals_repository

# def currently_in_use ():
#     in_use = []
#     current_rentals = rentals_repository.current_rentals()
#     all_vans = van_repository.select_all()
#     for van in all_vans:
#         if van.id in current_rentals:
#             in_use.append(van)
#     return in_use



