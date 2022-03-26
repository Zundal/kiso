# 2 진법으로 만드는 계산기
binary = input()

def mBinary(n):
    n = int(n)
    print(n%2)
    a = n//2
    print(n//2)
    while(n//2 == 1):
        return mBinary(a)

print(mBinary(binary))
# for x in binary[::-1]:
#     print(x)

# 100 3
# 10  2
# 1   1
# 0   0

# 2 88
# 2 44    0
# 2 22    0
# 2 11    0
# 2 5     1
# 2 2     1
# 2 1     0