# 한수란
#   각 자리수가 등차수열로 이루어진 수
# 123 147 555 공차가 일정하니 한수이다
# 1 ~ 99 까지는 한수 이다
# 그 이후의 수는 한수이기도 아니기도 하다
# 그러면 한수를 구하는 공식을 구해보자 
def getDifference(num):
    if num < 100:
        return num
    else:        
        checkerArr = [False] * num
        differenceCount = 0    

        for idx in range(num):
            checkerArr[idx] = numberDiffernceChecke(str(idx+1))

        for val in checkerArr:
            if(val==True):
                differenceCount = differenceCount + 1

        return differenceCount

def numberDiffernceChecke(num):
    result = False 
    if(len(num)>1):
        difference = int(num[0]) - int(num[1])
        for val in num:
            if((difference) == (int(num[0]) - int(val))):
                result = True
    return result

print(getDifference(110))