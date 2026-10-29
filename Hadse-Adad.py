import random,os
ad=random.randint(1,100)
def Check(x,ad,a):
    if x==ad :
        print("Affarin Dorost bood.Te`dade Hads(",a,")")
        return True
    elif x>ad :
        print("Bia Paein tar")
        return False
    elif x<ad :
        print("Boro Balatar")
        return False
# ==== حلقه اصلی بازی ====
a=0
while True:
    x = int(input("Yek adad hads bezan: "))
    os.system('cls')
    a=a+1
    # حالا تابع رو با دو تا ورودی صدا بزن
    if Check(x, ad,a) == True:
        break