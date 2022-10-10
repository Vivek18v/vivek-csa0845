size = float(input('No.of elements :'))
data = [float(input()) for i in range(1,size+1)]
mean = sum(data)/size
data.sort()
median = data[int(size/2)]
print('Mean :', '{:.2f}'.format(mean))
print('Median :',median)
print('Mode :',max(set(data),key = data.count))
