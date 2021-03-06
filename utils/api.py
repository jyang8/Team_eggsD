import string

#takes file as input, outputs a dictionary of keys from the file
#file should be in format (apiName, key/id)
#dictionary key = apiName, value = key/id
def getKeys(f):
    keys = {}
    f = open(f, 'r')
    for line in f:
        apiInfo = line.split(',')
        keys[apiInfo[0]] = apiInfo[1].strip(string.whitespace)
    keys.pop('apiName', None)
    return keys

#print(getKeys('keys.txt'))
