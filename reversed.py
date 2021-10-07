a, b= map(int, input().split())
list1 = list(str(a))
list2 = list(str(b))

list1.reverse()
list2.reverse()

view1 = "".join(list1)
view2 = "".join(list2) 

view1 = int(view1)
view2 = int(view2)

if view1 < view2 :
    print(view2)
else :
    print(view1)