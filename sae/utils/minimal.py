#Only a tool for initial DB Creation

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Minimal version off app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#Initialisation of DB
db = SQLAlchemy(app)