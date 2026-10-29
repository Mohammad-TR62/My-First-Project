num1=int(input("adade aval ra vared kon :"))
x = ""
while x not in ('+', '-', '*', '/'):
    x = input("Amalgar ra vared kon: ")
    if x not in ('+', '-', '*', '/'):
        print("Eshterah! Dobare vared kon.")
num2=int(input("adade dovom ra vared kon :"))
#r=num1+num2
if x == '+':
    r=num1+num2
    print(num1,x,num2,"=",r)
elif x == '-':
    r=num1-num2
    print(num1,x,num2,"=",r)
elif x == '*':
    r=num1*num2
    print(num1,x,num2,"=",r)
elif x == '/':
    if num2 == 0:
        print("Taghsim bar 0 Emkan pazir nist")
    else:
        r=num1/num2
        print(num1,x,num2,"=",r)