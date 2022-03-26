stack = []
ham = []
for x in range(5):
    if x<3:
        ham.append(int(input()))
    else :
        stack.append(int(input()))

sumResult = min(ham)

if stack[0] < stack[1]:
    sumResult += stack[0]
else :
    sumResult += stack[1]

print(sumResult-50)