'''
    python in 명령어를 잘쓰는 방법에 대해서 참고하자
'''
txt = list(input())
result = []

ask = 97
for i in range(26):
    if chr(ask) in txt:
        result.append(str(txt.index(chr(ask))))
    else:
        result.append('-1')
    ask+=1

print(" ".join(result))