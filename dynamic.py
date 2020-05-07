from flask import Flask, request
from flask_cors import CORS, cross_origin
from Login import Login
from Register import Register
from CallScraper import GetTok, GetLang, IfExists
from models import db, Acct
import psycopg2, random, hashlib, json, os

def dyn():

    try:
        rows = db.session.query(Acct.github_name).all()
        
        di = {}

        a = json.dumps([{"name": ip[0]} for ip in rows])
        return a 
        
    except Exception as error:
        print(error.orig.args)
        return error.orig.args
    


    

if __name__ =="__main__":
    dyn()