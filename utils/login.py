import sqlite3

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
