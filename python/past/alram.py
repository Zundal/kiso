a, b= map(int, input().split())

def hour(h):
    if h == 0 :
        h = 24
    rHour = h - 1
    
    return rHour
    
def calculator(h, m):
    if m>=45:
        normal = m 
    else :
        normal = 60 + m
    realMinute = normal - 45
    if realMinute>=15:
        realHour = hour(h)
    else :
        realHour = h
    return print(realHour, realMinute)

calculator(a, b)