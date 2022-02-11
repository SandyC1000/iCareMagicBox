""" Server.py for iCareMagicBox"""
from flask import (Flask, render_template, request, flash, session,
                    redirect, jsonify)
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
 


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
    user = crud.get_user_by_email(email)  #user Object attribute
   # query user by email, check if match email in table users and if password match.
    if user:
        flash(f"*** Hello {user.fname}!  Welcome back for more kindness.")
        
        session['User.user_id'] = user.user_id  # variable user(crud above)
    else:
        flash("User email not found.")
    # session['user'] = user
    return redirect("/")


@app.route("/register/api", methods=["POST"]) # new AJAX
def register_user_api():
    """Create a new user using JS AJAX."""
    # print(">>>> we are in route  /register/api")
    fname = request.json.get("fname")
    # print(f'fname {fname}')
    lname = request.json.get("lname")
    email = request.json.get("email")
    password= request.json.get("password")
    phone = request.json.get("phone")
    birthday = request.json.get("birthday")
    address = request.json.get("address")

    # print(f"user_name = {fname}")
    # print(f"user_email = {email}") 

    user = crud.create_user(fname, lname, email, password, phone, birthday, address)
    # flash("*** Successfully created new User!!")
    return  { "success": True, "status": "*** New user confirmed!"}


@app.route("/register", methods=["POST"]) # old HTML
def register_user():
    """Create a new user."""
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password= request.form.get("password")
    phone = request.form.get("phone")
    birthday = request.form.get("birthday")
    address = request.form.get("address")

    # print(f"user_name = {fname}")
    # print(f"user_email = {email}") 

    user = crud.create_user(fname, lname, email, password, phone, birthday, address)
    flash("*** Successfully created new User!!")
    return redirect("/")


@app.route("/users")
def list_users():
    """Display all users/customers"""
    user_list = crud.get_all_users()
    return render_template("all_users.html", user_list=user_list)    


@app.route("/recipients")
def list_recipients():
    """Display all recipients"""
    recipient_list = crud.get_all_recipients()
    return render_template("all_recipients.html", recipient_list=recipient_list)        


@app.route("/packages")
def list_packages():
    """Display all care packages v1.0
     -trying all care boxes v2.0 js
    """
    package_list = crud.get_all_packages()

    return render_template("all_careboxes.html", package_list=package_list)


@app.route("/packages/JSON")
def list_packages_JSON():
    """Display all
     -trying all care boxes v2.0 js
    JSON str 2 packages
    """
    # package_list = crud.get_all_packages()
    package_list = crud.get_packages_dicts()
    return jsonify(package_list)


@app.route("/package/<package_id>")
def display_packagedetail(package_id):
    package = crud.get_package_detail(package_id)
    session['package_id'] = package_id
#   return f"******{package_id}" #form of recipient
    return render_template("package_detail.html", package_id=package_id, package = package)
  

@app.route("/recipient", methods=["POST"])
def package_recipient():
    """Create a new recipient."""
    # print('************')
    # print('SESSION ------>', session)
    # print('************')
    
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    birthday = request.form.get("birthday")
    address = request.form.get("address")
    user_id = session['User.user_id']
    sentpackage_id = session['package_id']
    session['n_msg_customized'] = request.form.get("msg_customized")
    # print(f'////>>>/recipient : text box {msg_customized}')
    # print the recipients HERE!!
    # print("==>>RECIPIENT confirm:\n",fname, lname, email, phone, birthday, address,user_id, sentpackage_id)
    # print(f"type of fname == {type(fname)}")
    # print(f"type of email == {type(email)}")

    recipient = crud.create_recipient(fname, lname, email, phone, birthday, address, user_id)
   
    return redirect(f"/checkout/{recipient.recipient_id}")


@app.route('/checkout/<int:recipient>')
def checkout(recipient):

    user_id = session['User.user_id']
    user = crud.get_user_by_id(user_id)
    
    package_id = session['package_id']
    package = crud.get_package_detail(package_id) 

    msg_customized = session['n_msg_customized']
    # msg_customized = package.msg_default
    # msg_customized = request.form.get("msg_customized")
    # print(f'/checkoput = = =>>> text box {msg_customized}')
    # sent_price = package.price
    # add session date time - record for shipping 
    # print(f"==>>> ROUTE Checkout: {package.msg_default} ")
    recipient_id = recipient
    n_recipient = crud.get_recipient(recipient_id)
    # print(f">>> === recipient Sent Package Transaction ===  {recipient_id}")
    sentpackage = crud.create_sentpackage(msg_customized, user_id, package_id, recipient_id)
    # print(f">>> *** Created Sent Package Transaction ***  {sentpackage}")
    msg_customized = f'==>> *****  Dear {n_recipient.fname}, {msg_customized} !! \n Best regards,  {user.fname}'
    flash(msg_customized)
    
    # *** Twilio SMS - trial account - need to register Verified Caller IDs ***
    # message = client.messages.create(
    # to="+1"+str(n_recipient.phone),
    # from_="+16502279500",  # Twilio phone
    # body="*** Hello from iCareMagicBox!! ***"+msg_customized)

    return redirect("/")

# 1 - needs to activate ngrok for Twilio to send response via mobile chat - tested ok
# @app.route("/sms", methods=['GET', 'POST'])
# def incoming_sms():
#     """Send a dynamic reply to an incoming text message"""
#     # Get the message the user sent our Twilio number
#     body = request.values.get('Body', None)
#     print(f'+++++>>>> body texted back: {body}')
#     # Start our TwiML response
#     resp = MessagingResponse()

#     # Determine the right reply for this message
#     if body == 'Y':
#         resp.message("Great! we will send a Thank You Box for you!")

#     elif body == 'N':
#         resp.message("Enjoy your iCareMagicBox")

#     return str(resp)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)