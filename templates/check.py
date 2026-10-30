import sqlite3
con = sqlite3.connect("user.db")
r = con.execute("SELECT * FROM users")
print(r.fetchall())