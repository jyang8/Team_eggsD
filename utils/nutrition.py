import urllib2, json


def searchIngredient(ingredient):
    word = ingredient.replace("and", "&")
    word = word.replace(" ", "+")
    key = "EBKSGqBHwTf5Z4kUkDqkjeqK4gnL1nz1TNxMMRQl"
    link = "http://api.nal.usda.gov/ndb/search/?format=json&q=" + word + "&sort=r&max=25&ds=Standard Reference&offset=0&api_key=" + key
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

#print(searchIngredient("potdas"))

#print(getNutrition("01009"))
