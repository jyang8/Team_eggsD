import sqlite3, hashlib

# if username given matches a username in the database, return true
# else, return false
def userExists(user):
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    cmd = "SELECT * FROM accounts;"
    sel = c.execute(cmd)
    for record in sel:
        if user == record[0]:
            db.close()
            return True
    db.close()
    return False

# iList refers to a list of ingredients that users can add to
# which allows them to look for recipes incorporating those ingredients
def register(user, hashedPass):
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    cmd = "SELECT userID FROM accounts ORDER BY userID DESC;"
    sel = c.execute(cmd)
    userID = 1
    iList = ""
    for record in sel:
        userID = userID + record[0]
        break
    entry = "INSERT INTO accounts VALUES ('%s','%s','%d','%s');"%(user, hashedPass, userID, iList)
    c.execute(entry)
    db.commit()
    db.close()    

# if username and hashed password given match a username and its corresponding hashed password in the database, return true
# else, return false
def verify(user, hashedPass):
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    cmd = "SELECT * FROM accounts;"
    sel = c.execute(cmd)
    for record in sel:
        if user == record[0] and hashedPass == record[1]:
            db.close()
            return True
    db.close()
    return False

# returns the unique userID associated with a user account
def getUID(user):
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    id = ""
    cmd = "SELECT * FROM accounts;"
    sel = c.execute(cmd)
    for record in sel:
        if user == record[0]:
            id = record[2]
    db.close()
    return id

# returns a hashed version of the password
def hashPass(password):
    return hashlib.sha224(password).hexdigest()
    
# returns a user's hashed password
def getPass(userID):
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    cmd = "SELECT hashedPass FROM accounts WHERE userID = %d;"%(userID)
    sel = c.execute(cmd).fetchone()
    return sel[0]

# changes a user's hashed password
def changePass(newHashedPass, userID):
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    cmd = "UPDATE accounts SET hashedPass = '%s' WHERE userID = %d;"%(newHashedPass, int(userID))
    sel = c.execute(cmd)
    db.commit()
    db.close()

# returns the list of ingredients saved by a user
def getIList(userID):
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    cmd = "SELECT iList FROM accounts WHERE userID = %d;"%(int(userID))
    sel = c.execute(cmd).fetchone()
    return sel[0]

# adds an ingredient to the list of ingredients saved by a user
# delimiter for iList is a semicolon
# iList is ordered from oldest entry to newest entry
def addIngredient(i, userID):
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    tmp = getIList(userID) + i + ";"
    cmd = "UPDATE accounts SET iList = '%s' WHERE userID = %d;"%(tmp, int(userID))
    sel = c.execute(cmd)
    db.commit()
    db.close()

# if given ingredient is in the user's list, return true
# else, return false
def checkIngredient(i, userID):
    iList = getIList(userID)
    iList = iList[:len(iList)-1].split(";")
    for item in iList:
        if i == item:
            return True
    return False

def rmIngredient(i, userID):
    iList = getIList(userID)
    iList = iList[:len(iList)-1].split(";")
    newList = ""
    for item in iList:
        if i != item:
            newList += item + ";"
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    cmd = "UPDATE accounts SET iList = '%s' WHERE userID = %d;"%(newList, int(userID))
    sel = c.execute(cmd)
    db.commit()
    db.close()
