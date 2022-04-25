for loop1 in range(int(input())):
    arr = list(map(int, input().split(' ')))
    avg = int(sum(arr[1:])/arr[0])
    
    cnt = 0
    for i in arr[1:] :
        if i > avg:
            cnt = cnt + 1
    print("{:.3f}%".format(round((cnt/(len(arr[1:])))*100,3)))