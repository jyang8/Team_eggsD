from flask import Flask, render_template, session, redirect, url_for, request
import utils
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
    return render_template('home.html')

@app.route("/list/", methods = ["GET"])
def list():
    for (key in request.args):
        print key
    if ('ingredient' in request.args):
        
        list = nutrition.searchIngredient(request.args['ingredient']);
        return render_template('list.html', list = list)
    return redirect(url_for("new"))

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
