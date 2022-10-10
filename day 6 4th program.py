n=int(input("N="))
m=int(input("M="))
i=0
j=1
if(n>0):
    while(i<n):
        sum=0
        for h in range(1,j):
            if(j%h==0):
                sum=sum+h
        if(sum==j):
            i=i+1
            k=0
            h=0
            if(m>0):
                print("\nfirst",m,"factors of ",j,"are : ",end='')
                for b in range(1,j+1):
                    if(j%b==0):
                        if(h>m):
                            break
                        else:
                            print(b,end=' ')
                            h=h+1
            else:
                print("enter the valid number to find the factors")
        j=j+1
else:
    print("enter the valid number to find the perfect number ")

    
