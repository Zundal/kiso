def commonMulti(a, b):
    cnt = 1
    cal1 = 1
    while(True):
        
        if a%cnt == 0 and b%cnt==0 :
            cal1 = cal1 * cnt
            print(cal1)
        
        cnt += 1

cycle=int(input())
for x in range(cycle):
    a, b = map(int, input().split())
    
    
    commonMulti(a, b)


