"""Models for iCareMagicBox app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Classes in TABLES
class User(db.Model):
    """creating a user table """
    __tablename__ = "users"

    user_id = db.Column(db.Integer, 
                        autoincrement = True,
                        primary_key = True, )
    fname = db.Column(db.String(30),
                      nullable = False, unique = True, ) 
    lname = db.Column(db.String(30),
                      nullable = False, unique = True, )
    email = db.Column(db.String(30), 
                    nullable = False, unique = True, )
    password  = db.Column(db.String(10),
                    nullable = False, )
    phone  = db.Column(db.Integer,
                    nullable = False, )
    birthday  = db.Column(db.DateTime,
                nullable = False, )
    address  = db.Column(db.String(200),
                nullable = False, )            

    def __repr__(self):
        return f"""<User user_id = {self.user_id} 
                    fname = {self.fname}
                    lname = {self.lname}
                    email = {self.email} 
                    password = {self.password}
                    phone = {self.phone}
                    birthday = {self.birthday}
                    address = {self.address}>"""

class Recipient(db.Model):
    """ creating recipients table"""   
    __tablename__ = "recipients"

    recipient_id = db.Column(db.Integer, 
                        autoincrement = True,
                        primary_key = True, )
    fname = db.Column(db.String(30),
                      nullable = False, unique = True, ) 
    lname = db.Column(db.String(30),
                      nullable = False, unique = True, )
    email = db.Column(db.String(30), 
                    nullable = False, unique = True, )
    phone  = db.Column(db.Integer,
                    nullable = False, )
    birthday  = db.Column(db.DateTime,
                nullable = False, )
    address  = db.Column(db.String(200),
                nullable = False, )   
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),
                         nullable=False)
    sentpackage_id = db.Column(db.Integer, db.ForeignKey('sentpackages.sentpackage_id'),
                         nullable=False)

    user = db.relationship("User", backref="recipients")
    sentpackage = db.relationship("Sentpackage", backref="sentpackages")

    def __repr__(self):
        return f"""<Recipient recipient_id = {self.recipient_id} 
                    fname = {self.fname}
                    lname = {self.lname}
                    email = {self.email} 
                    phone = {self.phone}
                    birthday = {self.phone}
                    address = {self.address}
                    user_id = {self.user_id}
                    sentpackage_id = {self.sentpackage_id}>"""

class package(db.Model):
    """creating types of package table """
    __tablename__ = "packages"

    package_id = db.Column(db.Integer, 
                    autoincrement = True,
                    primary_key = True, )
    package_type = db.Column(db.String(30),
                    nullable = False, unique = True, ) 
    msg_default = db.Column(db.Text,
                    nullable = False, unique = True, )
    contents = db.Column(db.String(200), 
                    nullable = False, unique = True, )
          

    def __repr__(self):
        return f"""<Package package_id = {self.package_id} 
                    package_type = {self.package_type}
                    msg_default = {self.msg_default}
                    contents = {self.contents} >"""       

class Sentpackage(db.Model):
    """creating a sent package table"""
    __tablename__ = "sentpackages"

    sentpackage_id = db.Column(db.Integer, 
                        autoincrement = True,
                        primary_key = True, )
    msg_customized = db.Column(db.Text,
                        nullable = False,)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),
                         nullable=False,)
    package_id = db.Column(db.Integer, db.ForeignKey('packages.package_id'),
                         nullable=False,)

    user = db.relationship("User", backref="users")
    recipient = db.relationship("Recipient", backref="recipients")
    package = db.relationship("package", backref="packages")       

    def __repr__(self):
        return f"""<Sentpackage sentpackage_id = {self.sentpackage_id} 
                    msg_customized = {self.msg_customized}
                    user_id = {self.user_id}   
                    recipient_id = {self.recipient_id}            
                    package_id = {self.package_id} >""" 
  

def connect_to_db(flask_app, db_uri="postgresql:///sentpackages", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)
 
    print("Connected to the db!")
 


if __name__ == "__main__":
  #  from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
    from flask import (Flask, render_template, request, flash, session,
                    redirect)
    from jinja2 import StrictUndefined    
    app = Flask(__name__)
    app.secret_key = "dev"
    app.jinja_env.undefined = StrictUndefined

    
    connect_to_db(app)