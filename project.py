c =[["Dhruv","ID203",5000],
    ["Abhimanyu","ID101",2500], 
    ["Siddhu", "ID202",1000]]          
    


def cashwithdraw(ID):
    print("cashwithdraw")
    e = int(input("enter your withdrawal amount:"))
    for f in c:
        if f[1]==ID:
            print("Your remaining balance is "+str(f[2]-e))


def cashdeposit(ID):
    print("cashdeposit")
    d= int(input("enter your deposit amount:"))
    for f in c:
        if f[1]==ID:
            print("Your new balance is "+str(f[2]+d))

def checkbalance(ID):
    print("checkbalance")
    for f in c:
        if f[1]==ID:
            print("Your balance is "+str(f[2]))

I = input("Enter your ID:")
v = int(input("enter a number:"))

if v==1:
    cashwithdraw(I)
elif v==2:
    cashdeposit(I)
else:
    checkbalance(I)



