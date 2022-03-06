def overTimeCnt(defaultTime, appendTime):
    __resultTime = 0
    __resultMin = 0

    _append = appendTime.split()
    _default = defaultTime.split()

    __resultTime = int(_default[0]) + int(_append[0])
    __resultMin = int(_append[1]) + int(_default[1])

    if(__resultMin > 59): 
        __resultMin = __resultMin - 60
        __resultTime = __resultTime + 1
    if(__resultTime > 23): 
        __resultTime = __resultTime - 24
        
    return str(__resultTime) + ' ' + str(__resultMin) 

def appendTime (data):
    result = ''
    time = ''
    min = ''
    data = int(data)

    if(data > 60):    
        time = data//60
        min = data%60
        result = str(time) + ' ' + str(min)
        
    else:
        time = '0'
        min = data
        result = str(time) + ' ' + str(min)
        
    return result

# 훈제오리 시작 시간
inputTime = input()
# 훈제오리 요리시간
cookingTime = input()
resultcookingTime = appendTime(cookingTime)

print(overTimeCnt(inputTime, resultcookingTime))