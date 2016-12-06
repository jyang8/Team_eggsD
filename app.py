#from flask import Flask, render_template, session, redirect, url_for, request
#import flask
#import sqlite3
#import hashlib


app = Flask(__name__)

"""
app.secret_key

f = data/accounts.db
db = sqlite3.connect(f)
c = db.cursor()
#"""

@app.route("/", methods = ['GET'])
def new():
    return

"""
@app.route("/login/", methods = ['POST', 'GET'])
def login():
    return

@app.route("/authenticate/", methods = ['POST', 'GET'])
def authenticate():
    return

@app.route("/logout/")
def logout():
    return
#"""

if __name__ == "__main__":
    app.debug = True
    app.run()
