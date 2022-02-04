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
#    print (fake_fname, fake_lname)


#create packages
with open("data/packages.json") as f:
    package_data = json.loads(f.read())

# packages_in_db=[]
for package in package_data:
    package_type, msg_default, contents, price = (
        package["package_type"],
        package["msg_default"],
        package["contents"],
        package["price"]
    )
    crud.create_package(package_type, msg_default, contents, price)