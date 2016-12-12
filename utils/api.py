import string

def getKeys(f):
    keys = {}
    f = open(f, 'r')
    for line in f:
        apiInfo = line.split(',')
        keys[apiInfo[0]] = apiInfo[1].strip(string.whitespace)
    keys.pop('apiName', None)
    return keys

print(getKeys('keys.txt'))
