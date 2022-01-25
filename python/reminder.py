number = []
for num in range(10):
    number.append(int(input())%42)

print(len(set(number)))
