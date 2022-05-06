txt = list(input())
result = []

ask = 97
for i in range(26):
    if chr(ask) in txt:
        result.append(txt.index(chr(ask)))
    else:
        result.append(-1)
    ask+=1
print(result)