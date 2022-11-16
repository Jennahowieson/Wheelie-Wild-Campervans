import pdb
from models.customer import Customer
from models.van import Van
from models.rental import Rental

import repositories.van_repository as van_repository
import repositories.customer_repository as customer_repository
import repositories.rentals_repository as rental_repository

van_repository.currently_in_use ()

pdb.set_trace()
