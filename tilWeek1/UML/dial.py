x = input()
arr = {
'OPERATOR' : 11,
'W' : 10,
'X' : 10,
'Y' : 10,
'Z' : 10,
'T' : 9,
'U' : 9,
'V' : 9,
'P' : 8,
'Q' : 8,
'R' : 8,
'S' : 8,
'M' : 7,
'N' : 7,
'O' : 7,
'J' : 6,
'K' : 6,
'L' : 6,
'G' : 5,
'H' : 5,
'I' : 5,
'D' : 4,
'E' : 4,
'F' : 4,
'A' : 3,
'B' : 3,
'C' : 3
}
result = 0
for _ in x :
    result += arr[_]

print(result)