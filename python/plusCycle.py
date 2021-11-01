# 더하기 사이클
# https://www.acmicpc.net/problem/1110
'''
    예시
    26 => 
        2 + 6 = 8
        68
        6 + 8 = 14
        84
        8 + 4 = 12
        42 
        4 + 2 = 6
        26
    
'''
num = int(input())
temp = 0
def plusCycle(num):
    arr = []
    if num>=0 and num<=99 :
        arr = list(str(num))
        
        temp = int(arr[0]) + int(arr[1])
        
        print(str(arr[1])+str(str(temp)[::-1]))
    #     if num<10:
            
    #         pass
    #     else :
            
    #         pass
        
    #     result = 0
    #     return result 
    # else:
    #     return False
    pass

plusCycle(num)