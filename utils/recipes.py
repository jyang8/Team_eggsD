import urllib2, json

yid = "e3b721c8"

key = "3ee65fd50967cc9a8c8819d32fd8b1f9"

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

def info(recipe, info):
    ingredients = ""
    for ingredient in info[1]:
        ingredients += ingredient + ", "
    ingredients = ingredients.rstrip(", ")
    time = info[2]
    hour = time % 3600
    time -= hour * 3600
    minutes = time % 60
    time -= minutes * 60
    hour = str(hour)
    minutes = str(minutes)
    seconds = str(time)
    infoString = "Recipe for " + recipe + " by " + info[0] + ".\nInclude Ingredients:" + ingredients + "\nThis recipe takes " + hour + "hr " + minutes + "min " + seconds + "seconds"
    infoString.replace("\u0300", "")
    return infoString

def massInfo(recipes):
    information = ""
    for key in recipes.keys():
        information += info(key, recipes[key]) + "\n\n"
    return information
    
print(massInfo(getRecipe(["cognac", "garlic"], "onion soup")))

