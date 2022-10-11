a=[-1,-2,4,-2,5,2,5,-1]
count={}
print(a)
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print("frequency of each element")
for key,value in count.items():
    print(key," = ",value)
