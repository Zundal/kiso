result = int(input())
stack = []
for x in range(result):
    addNum = int(input())
    stack.append(addNum)

stack.sort()
stack.reverse()

for x in stack:
    print(x)