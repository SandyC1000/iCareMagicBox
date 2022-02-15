# iCareMagicBox

Project description:
- iCareMagicBox is an app built on a Flask server with a PostgreSQL database, with SQLAlchemy as the ORM. The front end templating uses Jinja2, the HTML was built using Bootstrap, and the Javascript uses AJAX to interact with the backend.The text message is built using Twilio API.

Database: Postgresql 
create database: createdb carepackages
(env) 🐳 hackbright@0109d1891da5:~/src/Hackbright/PROJECT/iCareMagicBox (main) $ psql carepackages
psql (13.5 (Ubuntu 13.5-2.pgdg20.04+1))
Type "help" for help.

carepackages=# \dt
             List of relations
 Schema |     Name     | Type  |   Owner    
--------+--------------+-------+------------
 public | packages     | table | hackbright
 public | recipients   | table | hackbright
 public | sentpackages | table | hackbright
 public | users        | table | hackbright
(4 rows)

## Technologies
**Tech Stack:**
- Python 3.8
- PostgreSQL
- Flask
- SQLAlchemy
- Jinja2
- HTML
- CSS
- Javascript
- AJAX
- JSON
- Bootstrap

Installation
Prerequisites
To run iCareMagicBox, install:
- Python 3.8
- PostgreSQL
- API for Twilio SMS text message
- Flask
 
Run iCareMagicBox on local computer
- Clone or fork repository:
$ git clone https://github.com/SandyC1000/iCareMagicBox.git
 
- Create and activate a virtual environment within iCareMagicBox directory:
$ git virtual env
$ source env/bin/activate
 
- Install dependencies:
$ pip3 install -r requirements.txt
 
- get an API key from Twilio by registering and creating a trial account,
 then add the API key to secrets.sh file and run:
$ source secrets.sh
 
-Run model.py to create all SQL database model and tables:
$ python3 model.py
 
-Run seed_database.py to create data in tables:
$ python3  seed_database.py
 
- Split terminal and run server.py on terminal to activate app:
$ python3 server.py
 
 
## For Version 2.0
- **Data validation:** will use Google Maps to check if the address is correct.
- **Password hashing:** Passwords will be hashed before being saved to the database.