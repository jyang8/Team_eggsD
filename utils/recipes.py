import urllib2, json

def getRecipe(ingredients, dish):
    dish = dish.replace(" ", "+")
    for index, ingredient in enumerate(ingredients):
        ingredients[index] = ingredients[index].replace(" ", "+")
    link = "http://api.yummly.com/v1/api/recipes?_app_id=YOUR_ID&_app_key=YOUR_APP_KEY&q=onion+soup&allowedIngredient[]=garlic&allowedIngredient[]=cognac"
    print(dish)

getRecipe(["hi", "two", "idjoa"], "this andosin asddhoia")

