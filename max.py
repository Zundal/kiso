arr = []
for _ in range(9):
    arr.append(int(input()))
    
result = max(arr)
print(result)
print(arr.index(result)+1)