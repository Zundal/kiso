def minute(n):
    if n >= 0 or n <=59 :
        if 0 > n - 45:
            return n + 60 - 45
        else :
            return n - 45
    
def hour(n):
    if 0 <= n or n <= 23:
        return n + 24 