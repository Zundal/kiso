stack = []
for x in range(5):
    a = int(input())
    if a<40:
        a = int(40)
    stack.append(a)
    
avgResult = int(sum(stack)/len(stack))
print(avgResult)