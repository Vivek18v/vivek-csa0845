def sumsquare(l):
    even=0
    odd=0
    for i in l:
       if i%2==0:
        even=even+i**2
       else:
        odd=odd+i**2
    l=[odd,even]
    return(l)
n=int(input("enter the number of elements:"))
l=[]
if(n>0):
    for i in range(n):
        m=int(input("enter the elements"))
        l.append(m)
print(sumsquare(l))
