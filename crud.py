
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

def get_user_by_id(user_id):
    """ return user info by user_id """ 
    return User.query.filter(User.user_id == user_id).first()


def create_package(package_type, msg_default, contents, price):
    package = Package(
            package_type = package_type,
            msg_default = msg_default,
            contents = contents,
            price = price )
    
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

def get_recipient(recipient_id):
    """ return recipient info by recipient_id """ 
    return Recipient.query.filter(Recipient.recipient_id == recipient_id).first()    

def get_all_packages():
    """ return all packages"""
    return Package.query.all()

def get_package_detail(package_id):
    """ return package by type """
    return Package.query.get(package_id) 

def create_sentpackage(msg_customized, user_id, package_id, recipient_id):
    """ return package by type """
    sentpackage = Sentpackage(
            msg_customized = msg_customized,
            user_id = user_id,
            package_id = package_id,
            # add shipping date time
 #           order_date = current_date
            recipient_id = recipient_id
            )
    print(f"=>=> Sentpackage details: {sentpackage}")
    print(f"oreder date   Shipping date")
    db.session.add(sentpackage)
    db.session.commit()
    return sentpackage
   
