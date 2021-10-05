listCnt=int(input())

for x in range(listCnt):
    result = 0
    cnt = 0
    valueList = input()
    for y in valueList:
        if y == 'O':
            cnt += 1
            result += cnt
        else :
            cnt = 0
    print(result)
        
