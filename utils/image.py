import urllib2, json

# Uses Clarifai's API

def getIngredient( url ):
    # entire url = head + url + end + token
    head = "https://api.clarifai.com/v1/tag?url=" 
    end = "&access_token="
    token = "8x4MflLoJTmzWWa7VQqrQuQkW9jJsU"
    newURL = head + url + end + token
    
    page = urllib2.urlopen( newURL ).read()
    d = json.loads( page )

u = "http://weknowyourdreams.com/images/pasta/pasta-04.jpg"
# getIngredient(u)

