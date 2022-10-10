def gcd(x,y):
    r=x%y
    if(r==0):
        return y
    else:
        return gcd(y,r)

n=int(input("enter the number value:"))
l=[]
for i in range(n):
    m=int(input("num="))
    l.append(m)
print(l)
if(n==3):
    f=[]
    for j in range(1,n):
        t=0
        t=gcd(l[j-1],l[j])
        f.append(t)
    print(f)
    for d in range(1,len(f)):
        gcd=gcd(f[d-1],f[d])
    print(gcd)
    a=1
    for s in l:
        a=a*s
        print("lcm=",a/gcd)
elif(n==2):
    for g in range(1,n):
        gcd=gcd(l[g-1],l[g])
    print("gcd=",gcd)
    a=1
    for s in l:
        a=a*s
    print("lcm=",a/gcd)
