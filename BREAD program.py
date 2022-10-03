n=int(input("Enter the number of fresh loves purchased : "))
m=int(input("Enter the number of day old loves purchased : "))
if(n>=0 and m>=0):
    print("Regular price: Rs.185.00")
    print("Amount of new loaves : ",n*185)
    print("Amount of day old loaves :",(m*185)-((m*185)*60/100))
    print("Total amount : ",n*185+(m*185)-((m*185)*60/100))
else:
    print("enter the positive ")
