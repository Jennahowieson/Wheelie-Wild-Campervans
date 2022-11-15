# from datetime import date
# import repositories.van_repository as van_repository
# import repositories.customer_repository as customer_repository

# def give_rental_options(id):
#         available_vans = []
#         customer = customer_repository.select(id)
#         vans = van_repository.select_all()
#         for van in vans:
#             if customer.friends < van.capacity:
#               available_vans.append(van.van_name)
#         return (available_vans)

