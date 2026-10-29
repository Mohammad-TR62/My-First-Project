import sqlite3,os
conn=sqlite3.connect("MDB.db")
conn.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone TEXT)")
s=input("Nam ra vared kon : ")
n=input("Shomareh ra vared kon : ")
conn.execute("INSERT INTO  contacts (name , phone) VALUES (?,?)" ,(s,n))
conn.commit()
conn.close