num=list(input())

if int(num[1]) >= 5 :
    num[0] = str(int(num[0]) + int(1))
    num[1] = '0'

print(int(''.join(num)))