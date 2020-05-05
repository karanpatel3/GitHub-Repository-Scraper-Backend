from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import os, hashlib

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Acct(db.Model):
    __tablename__ = 'acct_logins'
    userid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    github_name = db.Column(db.String)
    passw = db.Column(db.String)
    email = db.Column(db.String)
    bio = db.Column(db.String)
    city = db.Column(db.String)
    occupation = db.Column(db.String)
    access_token = db.Column(db.String)

class Users(db.Model):
    __tablename__ = 'users'
    userid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)