
""" CRUD opertations. """
from model import db, connect_to_db, User, Package, Recipient, Sentpackage

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

def create_package(package_type, msg_default, contents) :
    package = Package(
            package_type = package_type,
            msg_default = msg_default, 
            contents = contents)
    
    db.session.add(package)
    db.session.commit()
    return package

def get_all_packages():
    """ return all packages"""
    return Package.query.all()

def get_package_by_id(package_id):
    """ return package by id """
    return Package.query.get(package_id) 