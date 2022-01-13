
""" CRUD opertations. """
from model import db, connect_to_db, User # , Recipients, Packages, Sentpackages

def create_user(fname, lname, email, password, phone, birthday, address) :
    user = User(fname = fname,
                lname = lname,
                email = email,
                password = password,
                phone = phone,
                birthday = birthday,
                address = address
                 )
    db.session.add(user)
    db.session.commit()

    return user