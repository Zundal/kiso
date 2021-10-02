menNum = int(input())
menSize = []

for _ in range(menNum):
    size = input().split()
    menSize.append((size[0] , size[1]))

for i in menSize:
    rank = 1
    for j in menSize:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")