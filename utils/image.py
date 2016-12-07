import urllib2, json

# Uses Clarifai's API

def getIngredient(url):
    # entire url = head + url + end + token
    head = "https://api.clarifai.com/v1/tag?url=" 
    end = "&access_token="
    token = "8x4MflLoJTmzWWa7VQqrQuQkW9jJsU"
    newURL = head + url + end + token
    # returns the contents of the target webpage
    page = urllib2.urlopen(newURL).read()
    # converts json object string to dictionary
    d = json.loads(page)
    # returns the list of possible ingredients??
    iList = d["results"][0]["result"]["tag"]["classes"]
    return iList

'''
u = "http://weknowyourdreams.com/images/pasta/pasta-04.jpg"
print getIngredient(u)
listItem = getIngredient(u)[0]
print listItem


print getIngredient(u) Output:

[u'pasta', u'spaghetti', u'basil', u'dinner', u'lunch', u'food', u'macaroni', u'sauce', u'delicious', u'tomato', u'cuisine', u'no person', u'noodles', u'nutrition', u'meal', u'healthy', u'traditional', u'plate', u'pesto', u'dish']

print listItem Output:

pasta
'''
