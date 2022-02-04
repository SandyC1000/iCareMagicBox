# iCareMagicBox

Activate environment:
a. source env/bin/activate
a. source secrets.sh for Twilio API text msg
b. pip3 -r requirements.txt
c. run python3 seed_database.py for users and packages
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

carepackages=# SELECT * FROM packages;