from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
# from flask_security import Security, SQLAlchemyUserDatastore
import os, hashlib


app = Flask(__name__, template_folder='templates')
db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

class Acct(db.Model):
    __tablename__ = 'acct_logins'
    userid = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    github_name = db.Column(db.String, unique=True)
    passw = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    bio = db.Column(db.String)
    city = db.Column(db.String)
    occupation = db.Column(db.String)
    access_token = db.Column(db.String)

class Users(db.Model):
    __tablename__ = 'users'
    userid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

class Skills(db.Model):
    __tablename__ = 'user_skills'
    skillid = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String)
    byte_num = db.Column(db.Integer)
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'))
