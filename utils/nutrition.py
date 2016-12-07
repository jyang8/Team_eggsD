import urllib2, json

key = "EBKSGqBHwTf5Z4kUkDqkjeqK4gnL1nz1TNxMMRQl"

def searchIngredient(ingredient):
    link = "http://api.nal.usda.gov/ndb/search/?format=json&q=" + ingredient + "&sort=n&max=25&offset=0&api_key=" + key
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
    return 1

#print(searchIngredient("carrot"))
