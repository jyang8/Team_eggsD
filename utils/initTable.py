import sqlite3

# creating the table in the database
db = sqlite3.connect("data/database.db")
c = db.cursor()
cmd = "CREATE TABLE accounts(user TEXT, hashedPass TEXT, userID INTEGER, iList TEXT);"
c.execute(cmd)

db.commit()
db.close()
