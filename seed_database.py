""" Crearting Seed Database for iCareMagicBox"""

import os, json
from random import choice, randint
from datetime import datetime
import crud, model, server

os.system ('dropdb carepackages')

model.connect_to_db(server.app)
model.db.create_all()

with open("data/users.json") as f:
    user_data = json.load(f.read())   

#create users
users_in_db=[]
for user in user_data:
    fname, lname, email, password, phone, birthday, address =(
        user["fname"],
        user["lname"],
        user["email"], 
        user["password"],
        user["phone"],
        user["birthday"]"
        user["address"])

    db_user = crud.create_user(fname, lname, email, password, phone, birthday, address)    
    users_in_db.append(db_user)

