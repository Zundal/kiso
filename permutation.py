limitNum = int(input())

stack = []
def permutation(num):
    if num == 0 :
        return stack
    stack.append(num)
    return permutation(num - 1)

result = 1
for _ in permutation(limitNum):
    result *= _

print(result)