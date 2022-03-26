a, b = map(int, input().split())
stack = []
cnt = 1
while(len(stack) < 1000):
    for x in range(cnt):
        stack.append(cnt)
    cnt += 1

print(sum(stack[a-1:b]))