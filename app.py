from flask import Flask, render_template, session, redirect, url_for, request
from utils import nutrition, info, recipes, image, api, initTable, accounts
#import flask
#import sqlite3
#import hashlib


app = Flask(__name__)
ingredient = ""


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
    global ingredient
    if 'ingredient' in request.args:
        ingredient = request.args['ingredient']
        #print ingredient
        list = nutrition.searchIngredient(ingredient)
        return render_template('list.html', list = list)
    return redirect(url_for("new"))


@app.route("/info/", methods = ["GET"])
def info():
    global ingredient
    if 'selection' in request.args:
       	#print ingredient
        
        #print wikistuff
        '''
        wikiInfo = info.findArticle(ingredient)
        for item in wikiInfo:
            print item
        #'''
        
        #print nutrition
        '''
        nutritionIDs = nutrition.searchIngredient(ingredient)
        nutritions = nutrition.getNutrient(nutritionsIDs[request.args['selection']])
        print nutritions
        #'''
        
        #print recipes
        #'''
        
        #'''
        
        return render_template('info.html')
    return redirect(url_for("new"))


#"""
@app.route("/login/", methods = ['POST', 'GET'])
def login():
    return render_template('login.html')

@app.route("/authenticate/", methods = ['POST', 'GET'])
def authenticate(): 
    message = ""
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['pass']
        hashPass = accounts.hashPass(password)

        if 'login' in request.form:
            if accounts.verify(username, hashPass):
                session['username'] = username
                return redirect(url_for("new"))
        if 'register' in request.form:
            if not (accounts.userExists(username)):
                accounts.register(username, hashPass)
                message = "User has been successfully registered"
            else:
                message = "User already exists"

    return redirect(url_for("login", message = message))


@app.route("/logout/")
def logout():
    session.pop('username')
    return redirect(url_for("new"))

#"""

if __name__ == "__main__":
    app.debug = True
    app.run()

