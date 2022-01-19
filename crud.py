
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
def get_user_by_email(User,email):
    """ return user info ny email """
    user_id = ""
    User.query.all()
    if User.query.filter(User.email == email).first():
        user_id = User.query.get(User.user_id)
    else:
        return print("email {email} not found, please register !")
    return print(f" User_id  {user_id}  email {email}")

def create_package(package_type, msg_default, contents):
    package = Package(
            package_type = package_type,
            msg_default = msg_default,
            contents = contents)
    
    db.session.add(package)
    db.session.commit()
    return package

def create_recipient():
    recipient = Recipient(
    fname = request.form.get("fname"),
    lname = request.form.get("lname"),
    email = request.form.get("email"),
    phone = request.form.get("phone"),
    birthday = request.form.get("birthday"),
    address = request.form.get("address"),
    user_id = session["User.user_id"],
    sentpackage_id = sentpackage_id )

    db.session.add(recipient)
    db.session.commit()
    return recipient

def get_all_packages():
    """ return all packages"""
    return Package.query.all()

def get_package_detail(package_id):
    """ return package by type """
    return Package.query.get(package_id) 


