import urllib2, json

# Uses MediaWiki/Wikipedia's API

'''
exintro for just text before the first section

https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts|images&exlimit=1&explaintext&titles=
potato
&redirects=
'''

# returns a dictionary of the article page
def findArticle(item):
    # entire url = head + item + end
    head = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts|images&exlimit=1&explaintext&titles="
    end = "&redirects="
    newURL = head + item + end
    # returns the contents of the search
    page = urllib2.urlopen(newURL).read()
    # returns the article with the corresponding title
    d = json.loads(page)
    return d

# returns the pageID corresponding with each article, necessary to access the text content, as a string
def getPageID(article):
    s = article["continue"]["imcontinue"]
    pageID = ""
    for char in s:
        if char != "|":
            pageID += char
        else:
            return pageID

# returns the text content of the article as a string
def getArticle(article):
    return article["query"]["pages"][getPageID(article)]["extract"]

# returns the list of images in the article
def getImage(article):
    return article["query"]["pages"][getPageID(article)]["images"]

'''
https://en.wikipedia.org/w/api.php?format=json&action=query&titles=
File:BakedPotatoWithButter.jpg
&prop=imageinfo&iiprop=url
'''

# Note: file names with characters that have accent marks are problematic
#       because it cannot convert to ascii
# returns the url of the image given the file name
def getImageURL(img):
    head = "https://en.wikipedia.org/w/api.php?format=json&action=query&titles="
    end = "&prop=imageinfo&iiprop=url"
    newURL = head + img + end
    page = urllib2.urlopen(newURL).read()
    d = json.loads(page)
    return d["query"]["pages"]["-1"]["imageinfo"][0]["url"]

#print findArticle("potato")
#print getPageID(findArticle("potato"))
#print getArticle(findArticle("potato"))
#print getImage(findArticle("potato"))
#print getImageURL(getImage(findArticle("potato"))[1]["title"])
