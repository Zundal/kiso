def selfNum(n):
    return n+sum([int(i) for i in str(n)])

arr=[0]*10000
for i in range(10000):
    if(selfNum(i)<10000):
        arr[selfNum(i)]=1

for i in range(10000):
    if arr[i]==0:
        print(i)