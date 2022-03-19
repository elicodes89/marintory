import pdb
from models.user import User
from models.manufacturer import Manufacturer
from models.product import Product

import repositories.user_repository as user_repository
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

user_repository.delete_all()
manufacturer_repository.delete_all()
# product_repository.delete_all()

user_1 = User('Elisol', 'Shop Manager')
user_repository.save(user_1)

user_2 = User('Marcos' , 'Assistant')
user_repository.save(user_2)

manufacturer1 = Manufacturer('Marine Accesories,LTD.', 'marcos@marineaccesories.com', '01312225555', 'Accesories')
manufacturer_repository.save(manufacturer1)
manufacturer2 = Manufacturer('Marine Fish&Coral,LTD.', 'carolina@marinefishcoral.com', '01312225556', 'Live Stock')
manufacturer_repository.save(manufacturer2)
manufacturer3 = Manufacturer('Food for your stock,LTD.', 'mariana@stockfood.com', '01312225557', 'Food')
manufacturer_repository.save(manufacturer3)

# product1 = Product('Food for your stock,LTD.', 'mariana@stockfood.com', '01312225557', 'Food')
# manufacturer_repository.save(manufacturer3)


manufacturer1.name = "Eliseo"
manufacturer_repository.update(manufacturer1)
manufacturer1.email = "Eliseo@marineaccesories.com"
manufacturer_repository.update(manufacturer1)

for manufacturer in manufacturer_repository.select_all():
    print(manufacturer.__dict__)

# for product in product_repository.select_all():
#     print(product.__dict__)

pdb.set_trace()
