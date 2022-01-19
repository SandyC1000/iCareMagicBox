""" Serve.py for iCareMagicBox"""
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
    password = request.form.get("password")
    user = crud.get_user_by_email(User,email)
   # query user by email, check if match email in table users and if password match.
    if user:
        flash("Welcome back for more kindness.")
        session['user_id'] = 1 #
    else:
        
        flash("User email not found.")
    # session['user'] = user 
    
   
    return redirect("/")

@app.route("/register", methods=["POST"])
def register_user():
    """Create a new user."""
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password= request.form.get("password")
    phone = request.form.get("phone")
    birthday = request.form.get("birthday")
    address = request.form.get("address")

    print(f"user_name = {fname}")
    print(f"user_email = {email}") 

    user = crud.create_user(fname, lname, email, password, phone, birthday, address)
    return redirect("/")

@app.route("/packages")
def list_packages():
    """Display all care packages"""
    package_list = crud.get_all_packages()

    return render_template("all_carepackages.html", package_list=package_list)

# 1- write a template with a form to gather information about the recipient => recipient.html
# 2- render that template (with the reciepnt form) on @app.route("/package/<package_id>")
# 3 - give the form action="/recipient" 
# 4 - write/modifiy the route to handle the infomration sent in the html form
# 5 - print the information from the form so that you can see it in your terminal 
# 6 - print statements should look like print(f"recipent_name = {fname}")
# 7 - at this point, you are just testing out the routes and template to see that you can use them
# 8 - you are not yet adding the recipient to the db
# 9 - small amounts of code at a time == less places for bugs to hide :)


@app.route("/package/<package_id>")
def display_packagedetail(package_id):
    package = crud.get_package_detail(package_id)
    session['package_id'] = package_id
#   return f"******{package_id}" #form of recipient
    return render_template("package_detail.html", package_id=package_id, package = package)
  
@app.route("/recipient", methods=["POST"])
def package_recipient():
    """Create a new recipient."""
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    birthday = request.form.get("birthday")
    address = request.form.get("address")
    user_id = session['user_id']
    sentpackage_id = session['package_id']
   
    # print the recipients HERE!!
    print("==>>RECIPIENT confirm:\n",fname, lname, email, phone, birthday, address,user_id, sentpackage_id)
    print(f"type of fname == {type(fname)}")
    print(f"type of email == {type(email)}")

    recipient = crud.create_recipient(fname, lname, email, phone, birthday, address, user_id, sentpackage_id)

    return redirect("/checkout", recipient)

@app.route("/checkout")
def checkout(recipient):
    print(">>> *** Future Checkout Package Transaction ***  {recipient}")
    return redirect("/")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)