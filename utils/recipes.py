import urllib2, json

yid = ""

key = ""

def getRecipe(ingredients, dish):
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
            infoList = [recipe['sourceDisplayName'], recipe['ingredients'], recipe['totalTimeInSeconds'], recipe['smallImageUrls']]
            recipes[recipe['recipeName']] = infoList
        return recipes
    else:
        return "no matches"

getRecipe(["hi  ", "two", "idjoa"], "this andosin asddhoia")

