'''
    소인수분해
'''
literal = int(input())

divNum = 1
flag = True
while(literal >= divNum):
    if (literal % divNum == 0):
        literal = literal // divNum
        if(divNum!=1):
            print(divNum)
        if (divNum == 1):
            divNum += 1
        if(literal == divNum):
            print(divNum)
            flag = False
            break;
    else :
        divNum += 1
    
