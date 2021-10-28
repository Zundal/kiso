
# sumNum = 0
# def recul(num, result):
#     if num == 0:
#         return int(result)
#     result += num
#     return recul(num-1, result)
# inNum = int(input())
# print(recul(inNum, sumNum))

inNum = int(input())
def fibo(inNum):
    if inNum <= 1:
        return inNum
    return fibo(inNum-1) + fibo(inNum-2)
print(fibo(inNum))