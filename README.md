# iCareMagicBox

Project description
Tech stack
Features
Screenshots

Activate environment:
a. source env/bin/activate
a. source secrets.sh for Twilio API text msg
b. pip3 -r requirements.txt
   run python3 model.py to "Connected to the db!"
c. run python3 seed_database.py for users and packages
   split terminal
d. run python3 server.py


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
- Python
- Twilio API text message
- Flask
- SQLAlchemy
- Jinja2
- HTML
- CSS
- Javascript
- AJAX
- JSON
- Bootstrap


iCareMagicBox is an app built on a Flask server with a PostgreSQL database, with SQLAlchemy as the ORM. The front end templating uses Jinja2, the HTML was built using Bootstrap, and the Javascript uses AJAX to interact with the backend.The text message is built using Twilio API.

## For Version 2.0
- **Data validation:** will use Google Maps to chek if address is correct.
- **Password hashing:** Passwords will be hashed before being saved to the database