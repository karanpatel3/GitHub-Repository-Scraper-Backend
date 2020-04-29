from flask import Flask, request
from flask_cors import CORS, cross_origin
from Login import Login
from Register import Register
from CallScraper import GetTok, GetLang, IfExists
import psycopg2, random, hashlib, json

def dyn():

    try:
        connection = psycopg2.connect(host="localhost",database="test", user="karanpatel", password="")
        cur = connection.cursor()
        connection.autocommit = True
    except:
        print("Unable to Connect to Database")
    
    cur.execute("SELECT username FROM public.users")
    rows = cur.fetchall()
    
    di = {}

    a = json.dumps([{"name": ip[0]} for ip in rows])
    return a 
    

if __name__ =="__main__":
    dyn()