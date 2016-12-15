import urllib2, json

# Uses MediaWiki/Wikipedia's API


#exintro for just text before the first section

#https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts|images&exlimit=1&explaintext&titles=
#potato
#&redirects=


# en.wikipedia.org functions

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

# takes the article as a string and splits it into a list of sections
# returns the list of sections
def splitArticle(article):
    secList = article.split("\n\n\n")
    return secList
    
# https://en.wikipedia.org/w/api.php?format=json&action=parse&prop=sections&page=potato&redirects

# returns a list of the section titles of the article
def getSection(item):
    head = "https://en.wikipedia.org/w/api.php?format=json&action=parse&prop=sections&page="
    end = "&redirects="
    newURL = head + item + end
    page = urllib2.urlopen(newURL).read()
    d = json.loads(page)
    secTitles = []
    for entry in d["parse"]["sections"]:
        secTitles.append(entry["anchor"])
    return secTitles

# returns the number of sections in an article
def numSection(item):
    return len(getSection(item))
    
# returns a list with sublists consisting of [<section title>, <section content>]
def getArticleBySection(item, numSec):
    article = []
    ctr = 0
    while ctr <= numSec:
        head = "https://en.wikipedia.org/w/api.php?format=json&action=parse&prop=sections|text&page="
        mid = "&section="
        end = "&redirects="
        newURL = head + item + mid + str(ctr) + end
        page = urllib2.urlopen(newURL).read()
        d = json.loads(page)
        if ctr == 0:
            tmp1 = d["parse"]["title"]
        else:
            tmp1 = getSection(item)[ctr-1]
        tmp2 = d["parse"]["text"]["*"]
        tmp = [tmp1, tmp2]
        article.append(tmp)
        ctr += 1
    return article

# returns the list of images in the article
def getImage(article):
    return article["query"]["pages"][getPageID(article)]["images"]


#https://en.wikipedia.org/w/api.php?format=json&action=query&titles=
#File:BakedPotatoWithButter.jpg
#&prop=imageinfo&iiprop=url


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

def getAllImages(item):
    imgList = getImage(findArticle(item))
    allList = []
    for img in imgList:
        try: 
            allList.append(getImageURL(img["title"]))
        except Exception:
            pass
    return allList

#print findArticle("potato")
#print getPageID(findArticle("potato"))
#print getArticle(findArticle("potato"))
#print splitArticle(getArticle(findArticle("potato")))
#print "\n\n\n\n\n"
#print splitArticle(getArticle(findArticle("potato")))[0]
#print getSection("potato")
#print getArticleBySection("potato", numSection("potato"))
#print getImage(findArticle("potato"))
#print getImageURL(getImage(findArticle("potato"))[1]["title"])
print getAllImages("potato")

# --------------------------------------------------------------------------------------------------------------------------

# simple.wikipedia.org functions

# https://simple.wikipedia.org/w/api.php?format=json&action=parse&prop=images|sections|text&page=potato&section=0&redirects=

# returns a list of the section titles of the article
def getSectionS(item):
    head = "https://simple.wikipedia.org/w/api.php?format=json&action=parse&prop=images|sections|text&page="
    end = "&redirects="
    newURL = head + item + end
    page = urllib2.urlopen(newURL).read()
    d = json.loads(page)
    secTitles = []
    for entry in d["parse"]["sections"]:
        secTitles.append(entry["anchor"])
    return secTitles

# returns the number of sections in an article
def numSectionS(item):
    return len(getSectionS(item))

# returns a list with sublists consisting of [<section title>, <section content>]
def getArticleS(item, numSec):
    article = []
    ctr = 0
    while ctr <= numSec:
        head = "https://simple.wikipedia.org/w/api.php?format=json&action=parse&prop=images|sections|text&page="
        mid = "&section="
        end = "&redirects="
        newURL = head + item + mid + str(ctr) + end
        page = urllib2.urlopen(newURL).read()
        d = json.loads(page)
        if ctr == 0:
            tmp1 = d["parse"]["title"]
        else:
            tmp1 = getSectionS(item)[ctr-1]
        tmp2 = d["parse"]["text"]["*"]
        tmp = [tmp1, tmp2]
        article.append(tmp)
        ctr += 1
    return article

# returns a list of images in the article
def getImageS(item):
    head = "https://simple.wikipedia.org/w/api.php?format=json&action=parse&prop=images&page="
    end = "&redirects="
    newURL = head + item + end
    page = urllib2.urlopen(newURL).read()
    d = json.loads(page)
    return d["parse"]["images"]

# returns the URL of the image given the file name
def getImageURLS(img):
    head = "https://simple.wikipedia.org/w/api.php?format=json&action=query&titles=File:"
    end = "&prop=imageinfo&iiprop=url"
    newURL = head + img + end
    page = urllib2.urlopen(newURL).read()
    d = json.loads(page)
    return d["query"]["pages"]["-1"]["imageinfo"][0]["url"]


#print getSectionS("beef")
#print numSectionS("beef")
#print getArticleS("potato", numSectionS("potato"))
#print getImageS("beef")
#print getImageURLS(getImageS("beef")[0])
