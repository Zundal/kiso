def getDifference(num):
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