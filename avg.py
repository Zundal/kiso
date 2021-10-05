number = int(input())
arr = list(map(int, input().split()))

arr.sort()
mValue=arr[-1]
stack = []
for x in arr:
    stack.append(x/mValue*100)
print(sum(stack)/len(stack))