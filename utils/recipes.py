import urllib2, json

yid = 'e3b721c8'

key = '3ee65fd50967cc9a8c8819d32fd8b1f9'

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
            infoList = [recipe['sourceDisplayName'], recipe['ingredients'], recipe['totalTimeInSeconds'], recipe['smallImageUrls'], recipe['id']]
            recipes[recipe['recipeName']] = infoList
        return recipes
    else:
        return "no matches"

#returns extra information regarding a specific recipe given the id of the recipe, id can be found by searchRecipes
def getRecipe(idno):
    link = "http://api.yummly.com/v1/api/recipe/" + idno + "?_app_id=" + yid + "&_app_key=" + key
    u = urllib2.urlopen(link)
    D = json.loads(u.read())
    info = D['source']
    return info
    
#print(massInfo(getRecipe(["cognac", "garlic"], "onion soup")))
print(getRecipe('French-Onion-Soup-The-Pioneer-Woman-Cooks-_-Ree-Drummond-41364'))
