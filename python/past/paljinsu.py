# 1~7 까지 하고 넘기기
# 80 + 80 + 80 + 8 + 4 
# 800 + 800 + 800 + 800 + 80 + 8 + 8 + 2 
# 80 + 80 + 80 + 80 + 8 + 8 + 8 + 4 
# 800 + 800 + 80 + 80 + 8 + 8 + 8 + 8 + 8 + 5
# 8 진수를 10진수로 바꾸는 방법 => 마지막 자리수 빼고 정수 곱하기 8 == 8진수 

def digit(n):
    # 정수가 들어오면 자릿수 만큼 * 10
    if n == 0 : return ''
    else : return '0'*n 

def eightBinaryToNum(eightBinary):
    binary = list(str(eightBinary))
    binaryLen = len(binary)
    index = binaryLen
    
    tenBinary = 0
    
    for x in range(binaryLen):
        
        if (x+1) == binaryLen :
            tenBinary += int(binary[x])
        else :
            tenBinary += int(binary[x])*(8*int(('1'+digit(index-2))))        
        index-=1
    return tenBinary

# 10 => 2 + 2 + 2 + 2 + 2
# => 10 + 10 + 10 + 10 + 10
# => 100 + 100+ 10
# => 1010
def tenbinaryToBinary(tenBinary):
    # 10 진수를 2진수로 변환시킨다.
    binary = str(tenBinary/2)
    arr = binary.split('.')

    return 1
# TODO 바이너리 문제 https://www.acmicpc.net/problem/1212
# eightBinaryToNum(314)
# eightBinaryToNum(4122)
# eightBinaryToNum(434)
# eightBinaryToNum(2255)
