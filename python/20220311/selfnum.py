def func(number):
    result = int(number)
    for x in number :
        result = result + int(x)
    if(result<10000):    
        return result 

def checker():
    checkerArr = [False] * 10000
    for i in range(10000):
        idxnum = func(str(i))
        if(idxnum != None):
            checkerArr[idxnum] = True
    for idx, val in enumerate(checkerArr):
        if(val == False):
            print(idx)

checker()