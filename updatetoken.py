from flask import Flask, jsonify, request, json, jsonify
import json, os
from models import Acct, db

def UpToken(c):
    content = c
    gituser = content['userName']
    actoken = content['github_token']

    try:
        user = Acct.query.filter_by(username=gituser).one()
        user.access_token = actoken
        db.session.commit()
        result = 'true'
        message = "Your token has been updated."
        return message

    except Exception as error:
        print(error.orig.args)
        return error.orig.args