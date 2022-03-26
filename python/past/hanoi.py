inNum = int(input())
stack=[]
def hanoi(num, f_rom, to, other):
    if num == 0 :
        return
    hanoi(num - 1, f_rom, other, to)
    stack.append(str(f_rom) + ' ' + str(to))
    hanoi(num - 1, other, to, f_rom)
hanoi(inNum, 1, 3, 2)

print(len(stack))
for _ in stack:
    print(_)
