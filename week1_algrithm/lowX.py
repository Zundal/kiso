limit, x = input().split()
numArr = list(map(int, input().split()))

for _ in range(int(limit)):
    if int(numArr[_]) < int(x):
        print(numArr[_])