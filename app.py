from flask import Flask, render_template, session, redirect, url_for, request
from utils import nutrition, info, recipes, image, api, initTable
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

