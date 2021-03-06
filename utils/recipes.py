import urllib2, json, api

apiDict = api.getKeys('keys.txt')
yid = apiDict['yummlyID']
key = apiDict['yummlyKey']

#Returns a list of possible recipes given a set of ingredients and the dish you want to make
def searchRecipes(ingredients, dish):
    dish = dish.replace(" ", "+")
    ingString = ""
    for index, ingredient in enumerate(ingredients):
        ingredients[index] = ingredients[index].replace(" ", "+")
        ingString += "&allowedIngredient[]=" + ingredients[index]
    link = "http://api.yummly.com/v1/api/recipes?_app_id=" + yid + "&_app_key=" + key + "&q=" + dish + ingString
    u = urllib2.urlopen(link)
    D = json.loads(u.read())
    if 'matches' in D:
        recipes = {}
        for recipe in D['matches']:
            time = recipe['totalTimeInSeconds']
            hour = time / 3600
            minute = (time - (hour * 3600)) / 60
            if hour > 0:
                time = str(hour) + " hr " + str(minute) + " min"
            else:
                time = str(minute) + " min"
            infoList = [recipe['sourceDisplayName'], recipe['ingredients'], time, recipe['smallImageUrls'], recipe['recipeName']]
            recipes[recipe['id']] = infoList
        return recipes
    else:
        return "no matches"

#returns a list of possible dishes based on only the ingredient, this one does not require the user to know the dish they want to make
def getRecipes(ingredient):
    ingredient = ingredient.replace(" ", "+")
    link = "http://api.yummly.com/v1/api/recipes?_app_id=" + yid + "&_app_key=" + key + "&q=" + ingredient
    u = urllib2.urlopen(link)
    D = json.loads(u.read())
    if 'matches' in D:
        recipes = {}
        for recipe in D['matches']:
            time = recipe['totalTimeInSeconds']
            if time == None:
                time = "N/A"
            else:
                hour = time / 3600
                minute = (time - (hour * 3600)) / 60
                if hour > 0:
                    time = str(hour) + " hr " + str(minute) + " min"
                else:
                    time = str(minute) + " min"
            infoList = [recipe['sourceDisplayName'], recipe['ingredients'], time, recipe['smallImageUrls'], recipe['recipeName']]
            recipes[recipe['id']] = infoList
        return recipes
    else:
        return "no matches"
    
#returns extra information regarding a specific recipe given the id of the recipe, id can be found by searchRecipes
def getRecipe(idno):
    link = "http://api.yummly.com/v1/api/recipe/" + idno + "?_app_id=" + yid + "&_app_key=" + key
    u = urllib2.urlopen(link)
    D = json.loads(u.read())
    info = D['source']
    info['yield'] = D['yield']
    info['name'] = D['name']
    info['totalTime'] = D['totalTime']
    info['image'] = D['images'][0]['hostedMediumUrl']
    return info
    
#print(getRecipe('French-Onion-Soup-The-Pioneer-Woman-Cooks-_-Ree-Drummond-41364'))
#print(searchRecipes(['potato'], 'fries'))
#print(getRecipes("beef"))
