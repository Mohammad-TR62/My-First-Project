import os  # 👈 این خط رو اول برنامه اضافه کن

contacts = {}
while True:
    # 👈 این خط رو اینجا بذار تا هر بار که می‌خواد اسم بپرسه، صفحه رو پاک کنه
    os.system('cls') 
    
    nam = input("Nam ra vared kon: ")
    if nam.upper() == 'EXIT':
        break
        
    while True:
        phone = input("Shomare ra vared kon (11 ragham): ")
    
        if len(phone) != 11 or not phone.isdigit():
            print("Eshterah! Shomare bayad daghighan 11 ragham adadi bashe.")
            continue
            
        contacts[nam] = phone
        print("Shomareye" , phone ," Be name " , nam , " Ezafeh shod.") 
        break
        
print("--- Liste Contacts ---")
print(contacts)

# حالا از کاربر بپرس کی رو میخواد
esm = input("Esme ki ro mikhai peyda koni? ")
if esm in contacts:
    print("Shomare:", contacts[esm])
else:
    print("Peyda nashod!")      
    