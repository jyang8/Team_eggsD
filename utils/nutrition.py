import urllib2, json, api

key = api.getKeys('keys.txt')['usda']

#provides a list of food item related to the search term
def searchIngredient(ingredient):
    word = ingredient.replace("and", "&")
    word = word.replace(" ", "+")
    link = "http://api.nal.usda.gov/ndb/search/?format=json&q=" + word + "&ds=Standard+Reference&sort=r&max=25&offset=0&api_key=" + key
    u = urllib2.urlopen(link)
    D = json.loads(u.read())
    if 'list' in D.keys():
        d = D['list']
        ingredients = {}
        for item in d['item']:
            ingredient = item['name']
            l = ingredient.rsplit(',', 1)
            ingredient = l[0]
            ingredients[ingredient] = item['ndbno']
        return ingredients
    else:
        return "Search Not Found!"

#returns nutrition facts, idN is found through searchIngredients
def getNutrition(idN):
    link = "http://api.nal.usda.gov/ndb/nutrients/?format=json&api_key=" + key + "&nutrients=205&nutrients=204&nutrients=208&nutrients=269&ndbno=" + idN
    u = urllib2.urlopen(link)
    D = json.loads(u.read())
    d = D['report']['foods'][0]['nutrients']
    nutrition = {}
    for nutrient in d:
        value = nutrient['value'] + " " + nutrient['unit']
        nutrition[nutrient['nutrient']] = value
    return nutrition

#print(searchIngredient("potato"))

#print(getNutrition("01009"))
