n=int(input("x="))
if(n>0):
    for i in range(1,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(i**2+j**2==k**2):
                    print(i,j,k)
else:
    print("enter the values greater than 0")
