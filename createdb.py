#Creation of initial database

#Importing database from minimal app
from sae.utils.minimal import db

#creating DB
db.create_all()