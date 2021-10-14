a = input()
stack = []
for _ in a:
    stack.append(_)

stack.sort()
stack.reverse()
result = ''
for _ in stack :
    result += _

print(result)