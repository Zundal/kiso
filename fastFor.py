import sys
limit = int(input())
for x in range(limit):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)