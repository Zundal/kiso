# star = int(input())
# tab = star - 1
# starMark = ''

# for _ in range(star):
#     empty = tab * ' '
#     starMark += '*'
#     print(empty + starMark)
#     tab = tab - 1


score = int(input())

if score >= 90 and score <= 100:
    print('A')
elif score >= 80 and score <= 89:
    print('B')
elif score >= 70 and score <= 79:
    print('C')
elif score >= 60 and score <= 69:
    print('D')
else:
    print('F')