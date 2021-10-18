# https://www.acmicpc.net/problem/1181
num = int(input())
wStack = []
for x in range(num):
    wStack.append(input())

sortStack = []
for x in range(len(wStack)):
    temp = wStack[x]
    for y in range(len(wStack)):
        if temp < wStack[y]:
            wStack[x] = wStack[y]
            wStack[y] = temp
            print(temp)
            
print(wStack)