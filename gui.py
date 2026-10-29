import sqlite3,tkinter as tk
from tkinter import messagebox
con=sqlite3.connect("MD.db")
con.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone TEXT)")
#-------------------------- Tavabe`e ------------------------------------
def RGB():    
    lb_Er.place_forget()
    lb_Er2.place_forget()

def Save():
    nam=En.get()
    phone=En2.get()
    if  nam and phone :
        con.execute("INSERT INTO  contacts (name , phone) VALUES (?,?)" ,(nam,phone))
        con.commit()
        En.delete(0,tk.END)
        En2.delete(0,tk.END)
        En.config(bg="white") 
        En2.config(bg="white")
    else :
        lb_Er.place(x=400,y=40)
        lb_Er2.place(x=400,y=75)
        root.after(5000,RGB)
def Exit_ap():
    root.destroy()
def Del_ap():
    m=messagebox.askokcancel("Hazf","Aya Motmaen Hasti?")
    if m :
        s=En.get()
        con.execute("DELETE FROM contacts WHERE name = ?" ,(s,))
        con.commit()
        messagebox.showinfo("Delete","Karbar Hazf Shod") 
def ShA_ap():
    ListBox.delete(0,tk.END)
    cursor=con.execute("SELECT * FROM contacts")
    rows=cursor.fetchall()
    for row in rows :
        ListBox.insert(tk.END,row)
def Search_ap():
    s = En.get()
    r = con.execute("SELECT phone FROM contacts WHERE name = ?", (s,))
    c = r.fetchone()
    
    if c:
        En2.delete(0, tk.END)
        En2.insert(0, c[0])  # 👈 فقط خود متن شماره
    else:
        messagebox.showinfo("Search", "Peyda Nashod!")
def Update_ap():
    s = En.get()
    n = En2.get()
    con.execute("UPDATE contacts SET phone = ? WHERE name = ?", (n,s))
    con.commit()
    messagebox.showinfo("Update", "Update Shod")      
# ------------------------- User Form ----------------------------
root=tk.Tk()
root.title("Test")
root.attributes('-fullscreen', True) # یا root.state('zoomed')
#root.geometry("400x300+100+100")
#-------------------------- Labels ----------------------------
lb=tk.Label(root,text="Nam : ",font=("Arial", 14 ))
lb.place(x=100,y=30)
lb2=tk.Label(root,text="Tel : ",font=("Arial", 14 ))
lb2.place(x=100,y=60)
lb_Er=tk.Label(root,text="Nabayad Khali Basheh!!!",fg="Red")
#lb_Er.place(x=400,y=40)
lb_Er2=tk.Label(root,text="Nabayad Khali Basheh!!!",fg="Red")
#lb_Er2.place(x=400,y=75)
#--------------------------- Text Box s -------------------------
En=tk.Entry(root,font=("Arial",14))
En.place(x=160,y=35)
En2=tk.Entry(root,font=("Arial",14))
En2.place(x=160,y=70)
#----------------------- Buttons --------------------------------
btn_Save=tk.Button(root,text="Save",font=("Arial", 14),command=Save)
btn_Save.place(x=100,y=100)
btn_Del=tk.Button(root,text="Delete",font=("Arial",14),command=Del_ap)
btn_Del.place(x=160,y=100)
btn_SA=tk.Button(root,text="Show All",font=("Arial",14),command=ShA_ap)
btn_SA.place(x=233,y=100)
btn_Exit=tk.Button(root,text="Exit",font=("Arial",14),command=Exit_ap)
btn_Exit.place(x=323,y=100)
btn_Search=tk.Button(root,text="Search",font=("Arial",14),command=Search_ap)
btn_Search.place(x=100,y=138)
btn_Update=tk.Button(root,text="Update",font=("Arial",14),command=Update_ap)
btn_Update.place(x=177,y=138)
# ----------------------- ListBoxs ----------------------------------
ListBox=tk.Listbox(root,font=("Arial",14))
ListBox.place(x=50,y=200)

root.mainloop()