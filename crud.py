
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

#1/18/22 - take email, return a user object!
# SQLAlchemey to query user based on email
# run crud interactivetly to check on user
#return user object
# File "/home/hackbright/src/Hackbright/PROJECT/iCareMagicBox/server.py", line 87, in package_recipient
def get_user_by_email(email):
    """ return user info ny email """ 
    return User.query.filter(User.email == email).first()

def create_package(package_type, msg_default, contents):
    package = Package(
            package_type = package_type,
            msg_default = msg_default,
            contents = contents)
    
    db.session.add(package)
    db.session.commit()
    return package

def create_recipient(fname, lname, email, phone, birthday, address, user_id):
    recipient = Recipient(
            fname = fname,
            lname = lname,
            email = email,
            phone = phone,
            birthday = birthday,
            address = address,
            user_id = user_id )

    db.session.add(recipient)
    db.session.commit()
    return recipient

def get_all_packages():
    """ return all packages"""
    return Package.query.all()

def get_package_detail(package_id):
    """ return package by type """
    return Package.query.get(package_id) 


