n=int(input("enter the number of rows:"))
m=1
for i in range(1,n+1):
    for j in range(1,i+1):
     print(m,end=" ")
     m=m+1
    print()
    if (n<=0):
     print("no value is there:")
    else:
        print()
