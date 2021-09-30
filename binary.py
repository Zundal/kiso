'''
    10 진수 2진수 변화 코드
    2진수 10진수 변화 코드
    2진수 16진수 변화 코드
    16진수 2진수 변화코드
'''
from collections import deque
class binaryChanger:
    
    
    def numTobinary(self,n): # 숫자를 2진수로
        deq = deque()
        cnt = 0 
        for _ in range(n):
            cnt = cnt + 1
            if cnt == 2:
                deq.append('0')
                cnt = 0
                continue
            # elif deq[:] == 0 :
            #     deq.pop()
            #     deq.append('1')
        print(deq)
        pass
    
    def binaryToNum(self, n): # 2진수를 숫자로
        pass
    
    def numToHexadecimal(self, n): # 숫자를 16진수로
        pass
    
    def hexadecimalToNum(self, n): # 16진수를 숫자로
        pass

cbin = binaryChanger()
cbin.numTobinary(3)
#cbin.binaryToNum()
#cbin.numToHexadecimal()
#cbin.hexadecimalToNum()

