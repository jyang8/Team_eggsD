import urllib2, json, api

# Uses Clarifai's API

key = api.getKeys("keys.txt")["clarifai"]

# converts a decimal to a percent with accuracy of one decimal place
def decToPercent(num):
    return str(round(num * 100, 1)) + "%"

# returns a dictionary of ingredients given an image url
# key = ingredient
# value = probability 
def getIngredient(url):
    # entire url = head + url + end + token
    head = "https://api.clarifai.com/v1/tag?url=" 
    end = "&access_token="
    token = key # insert API key here
    newURL = head + url + end + token
    # returns the contents of the target webpage
    page = urllib2.urlopen(newURL).read()
    # converts json object string to dictionary
    d = json.loads(page)
    # returns the list of possible ingredients??
    iList = d["results"][0]["result"]["tag"]["classes"]
    pList = d["results"][0]["result"]["tag"]["probs"]
    i = {}
    ctr = 0
    while ctr < len(iList):
        i[iList[ctr]] = decToPercent(pList[ctr])
        ctr += 1
    return i


#u = "http://weknowyourdreams.com/images/pasta/pasta-04.jpg"
#print getIngredient(u)
#listItem = getIngredient(u)[0]
#print listItem

'''
print getIngredient(u) Output:

[u'pasta', u'spaghetti', u'basil', u'dinner', u'lunch', u'food', u'macaroni', u'sauce', u'delicious', u'tomato', u'cuisine', u'no person', u'noodles', u'nutrition', u'meal', u'healthy', u'traditional', u'plate', u'pesto', u'dish']

print listItem Output:

pasta
'''
