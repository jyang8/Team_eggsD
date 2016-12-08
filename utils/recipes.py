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
    print(ingString)

getRecipe(["hi  ", "two", "idjoa"], "this andosin asddhoia")

