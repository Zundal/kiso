limit = int(input())
for _ in range(limit):
    a, b= map(int, input().split())
    print('Case #',_+1,': ',a,' + ',b,' = ',a+b, sep='')