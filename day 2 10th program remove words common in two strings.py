str1=input("enter first string")
str2=input("enter second string")
a=set(str1.split())
b=set(str2.split())
common=list(a.intersection(b))
def remove(str1):
    str1=str1.split()
    s=[]
    for i in str1:
        if i not in common:
            s.append(i)
    return s
print(remove(str1))
print(remove(str2))
