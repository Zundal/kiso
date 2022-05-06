code = {
	"a":True, 
	"b":True, 
	"c":True, 
	"c=":True,
	"c-":True,
	"dz=":True,
	"d-":True,
	"lj":True,
	"nj":True,
	"s=":True,
	"z=":True,
	"e":True, 
	
	"k":True,
	"d":True
}

# if "nj" in "ljes=njak":
#     print(True)

# if 1 in [1,2,3,4]:
# 	print(True)
cnt = 0
for element in code:
	if element in "nljj":
    # print(True)
		print(code[element])
		cnt+=1
print(cnt)