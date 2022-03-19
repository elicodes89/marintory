import pdb
from models.user import User

import repositories.user_repository as user_repository

user_repository.delete_all()

user_1 = User('Daniel', 'Shop Assistant2')
user_repository.save(user_1)
user_2 = User('David' , 'Assistant')
user_repository.save(user_2)


pdb.set_trace()
