import urllib2, json

key = "EBKSGqBHwTf5Z4kUkDqkjeqK4gnL1nz1TNxMMRQl"

def searchIngredient(ingredient):
    word = ingredient.replace("and", "&")
    link = "http://api.nal.usda.gov/ndb/search/?format=json&q=" + word + "&sort=n&max=25&offset=0&api_key=" + key
    u = urllib2.urlopen(link)
    D = json.loads(u.read())
    d = D['list']
    ingredients = {}
    for item in d['item']:
        ingredient = item['name']
        l = ingredient.rsplit(',', 1)
        ingredient = l[0]
        ingredients[ingredient] = item['ndbno']
    return ingredients

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

print(searchIngredient("potato and pumpkin"))

#print(getNutrition("01009"))
