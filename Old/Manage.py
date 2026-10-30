import sqlite3
con=sqlite3.connect("MD.db")
con.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone TEXT)")
while True :
    print("-----   Menu   -----")
    print("\n 1. Ezafe kardan karbar (Create)")
    print("\n 2. Namayesh hame (Read)")
    print("\n 3. Taghir shomare (Update)")
    print("\n 4. Hazf karbar (Delete)")
    print("\n 5. Khorooj (Exit)")
    try :
        choice=int(input("\n Lotfan yek gozine ra entekhab kon:"))
    except :
        print("!!!!Eshtebah!!!!")
        continue 
    if choice==1 :
        s=input("Nam ra vared kon : ")
        n=input("Shomareh ra vared kon : ")
        con.execute("INSERT INTO  contacts (name , phone) VALUES (?,?)" ,(s,n))
        con.commit()
    elif choice==2 :
        print("\n ========LISTE CONTACTS ========")
        curser=con.execute("SELECT * FROM contacts ")
        rows=curser.fetchall()
        for row in rows :
           print(row)
    elif choice==3 :
        s=input("Nami ke Mikhahid Shomare ra Avaz Konid Ra vared kon : ")
        n=input("Shomareye Jadid ra vared kon : ")
        con.execute("UPDATE contacts SET phone = ? WHERE name = ?" ,(n,s))
        con.commit()
    elif choice==4 :
        s=input("Nami ke Mikhahid Hazf Konid Ra vared kon : ")
        con.execute("DELETE FROM contacts WHERE name = ?" ,(s,))
        con.commit()
    elif choice==5 :
        break
con.close()