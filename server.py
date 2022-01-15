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
    return redirect("/")

@app.route("/packages")
def list_packages():
    """Display all care packages"""
    package_list = crud.get_all_packages()
    return render_template("all_carepackages.html", package_list=package_list)

# write a template with a form to gather information about the recipient => recipient.html
# render that template (with the reciepnt form) on @app.route("/package/<package_id>")
# give the form action="/recipient" 
# write/modifiy the route to handle the infomration sent in the html form
    # print the information from the form so that you can see it in your terminal 
    # print statments should look like print(f"recipenjt_name = {fname}")
# at this point, you are just testing out the routes and tempate to see that you can use them
    # ytou are noit yet adding the recipient to the db
# small amounts of code at a time == less places for bugs to hide :)


@app.route("/package/<package_id>")      #package_id 
def display_packagedetail(package_id):


    package = crud.get_package_detail(package_id)
#   return f"******{package_id}" #form of recipient
    return render_template("package_detail.html", package_id=package_id, package = package)
  
@app.route("/recipient")
def package_recipient(user_id, sentpackage_type):
    """Create a new recipient."""
    fname = request.form.get("fname"),
    lname = request.form.get("lname"),
    email = request.form.get("email")
    phone = request.form.get("phone"),
    birthday = request.form.get("birthday"),
    address = request.form.get("address")
    user_id= request.args.get(user_id)
    sentpackage_id = request.args.get(sentpackage_id)


    recipient = crud.create_recipient(fname, lname, email, phone, birthday, address, user_id, sentpackage_id)

    return redirect("/buy_transaction", recipient)

@app.route("/buy_transaction", methods=["POST"])
def buy_transaction(recipient):
    print(">>> *** Future Buy Package Transaction ***")
    return redirect("/")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)