""" Crearting Seed Database for iCareMagicBox"""

import os, json
from random import choice, randint
from datetime import datetime
from faker import Faker
import crud, model, server

os.system ('dropdb carepackages')
os.system ('createdb carepackages')

model.connect_to_db(server.app)
model.db.create_all()

fake = Faker()
fake_fname = []
fake_lname = []
for n in range (5):
    fname = fake.unique.first_name()
    lname = fake.unique.last_name()
    email = f'{fname}.{lname}@gmail.com'.lower()
    password = f'password{n}'
    phone = fake.phone_number()
    birthday = fake.date()
    address = fake.address()
    
    crud.create_user(fname, lname, email, password, phone, birthday, address)    
#    users_in_db.append(db_user)
    

# print (fake_fname, fake_lname)    


# with open("data/users.json") as f:
#     user_data = json.loads(f.read()) 

#create users
# users_in_db=[]
# for user in user_data:
#     fname, lname, email, password, phone, birthday, address = (
#         user["fname"],
#         user["lname"],
#         user["email"],
#         user["password"],
#         user["phone"],
#         user["birthday"],
#         user["address"])

#     db_user = crud.create_user(fname, lname, email, password, phone, birthday, address)    
#     users_in_db.append(db_user)

# with open("data/recipients.json") as f:
#     recipient_data = json.load(f.read()) 

# recipients_in_db=[]
# for recipient in recipient_data:
#     fname, lname, email, phone, birthday, address, user_id, sentpackage_id =(
#         user["fname"],
#         user["lname"],
#         user["email"], 
#         user["phone"],
#         user["birthday"],
#         user["address"],
#         user["user_id"],
#         user["sentpackage_id"])

          
#     db_recipients = crud.create_user(ffname, lname, email, phone, birthday, address, user_id, sentpackage_id)    
#     recipients_in_db.append(db_recipients)

# #create packages
# packages_in_db=[]
# for package in package_data:
#     package_id, package_type, msg_default, contents = (
#         user["package_id"],
#         user["package_type"],
#         user["msg_default"], 
#         user["contents"],)
          
#     db_packages = crud.create_package(package_id, package_type, msg_default, contents)    
#     recipients_in_db.append(db_packages)

# #create sentpackages
# sentpackages_in_db=[]
# for sentpackage in sentpackage_data:
#     sentpackage_id, msg_customized, user_id, recipient_id, package_id  = (
#         sentpackage["sentpackage_id"],
#         sentpackage["msg_customized"],
#         sentpackage["user_id"], 
#         sentpackage["recipient_id"], 
#         sentpackage["package_id"],)
          
#     db_sentpackages = crud.create_sentpackage(sentpackage_id, msg_customized, user_id, recipient_id, package_id)    
#     recipients_in_db.append(db_sentpackages)  
