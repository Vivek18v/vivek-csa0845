def countstrings(n,start):
    if n==0:
        return 1
    count=0
    for i in range(start,5):
        count=count+countstrings(n-1,i)
    return count
def countvowelstrings(n):
    return countstrings(n,0)
n=int(input("enter input:"))
if(n>0):
    print(countvowelstrings(n))
else:
    print("enter positive numbers")
