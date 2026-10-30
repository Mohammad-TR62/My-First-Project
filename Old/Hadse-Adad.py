import random,os
ad=random.randint(1,100)
def Check(x,ad,a):
    if x==ad :
        print("Affarin Dorost bood.Te`dade Hads(",a,")")
        return True
    elif x>ad :
        print("Bia Paein tar")
        Save(x,a)
        return False
    elif x<ad :
        print("Boro Balatar")
        Save(x,a)
        return False
def Save(x,a):
    file = open("score.txt", "a")
    file.write(" Hadse " + str(a) + " = " + str(x) + "\n")
    file.close()
# ==== حلقه اصلی بازی ====
a=0
file = open("score.txt", "a")
file.write("========================================================================" + "\n")
file.write("Adade Dorost = " + str(ad) + "\n")
file.close()
while True:
    x = int(input("Yek adad hads bezan: "))
    os.system('cls')
    a=a+1
    # حالا تابع رو با دو تا ورودی صدا بزن
    if Check(x, ad,a) == True:
        Save(x,a)
        break