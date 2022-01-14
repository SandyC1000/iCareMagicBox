# print ("===>>> SERVER.py <====")
from flask import (Flask, render_template, request, flash, session,
                    redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined  

app = Flask(__name__)   #instance of Class Flask
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """Home Page Route"""
    return render_template("homepage.html")

@app.route("/login", methods=["POST"])
def login_user():
    """Create a new user."""
    email = request.form.get("email")
    password= request.form.get("password")
    user = crud.get_user_by_email(email, password)
   # query user by email, check if match email in table users and if password match.
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        crud.create_user(email, password)
        flash("Success! User has been created. Please log in.")
    return redirect("/")    

@app.route("/register", methods=["POST"])
def register_user():
    """Create a new user."""
    fname = request.form.get("fname"),
    lname = request.form.get("lname"),
    email = request.form.get("email")
    password= request.form.get("password")
    phone = request.form.get("phone"),
    birthday = request.form.get("birthday"),
    address = request.form.get("address")

    user = crud.create_user(fname, lname, email, password, phone, birthday, address)
    # if user:
    #     flash("Cannot create an account with that email. Try again.")
    # else:
    #     crud.create_user(fname, lname, email, password, phone, birthday, address)
    #     flash("Success! User has been created. Please log in.")
    return redirect("/")

@app.route("/packages")
def list_packages():
    """Display all care packages"""
    package_list = crud.get_all_packages()
    return render_template("all_carepackages.html", package_list=package_list)
    
    # package_id = request.form.get("package_id"),
    # package_type = request.form.get("package_type"),
    # msg_default = request.form.get("msg_default")
    # contents= request.form.get("contents")
          
#  CRUD will do init
#  db_packages = crud.create_package(package_id, package_type, msg_default, contents)    
#     
    # package = (package_id, package_type, msg_default, contents)
  
    # return redirect("/buy_transaction")

@app.route("/buy_transaction", methods=["POST"])
def buy_transaction():
    print(">>> *** Future Buy Package Transaction ***")
    return redirect("/")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)