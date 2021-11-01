limit = int(input())
for x in range(limit):
    print('*'*(x+1))

for x in reversed(range(limit-1)):
    print('*'*(x+1))