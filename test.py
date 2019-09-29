
def test1(x,y):
	a = 1
	b = "hello"
	print("inner : ")
	print(locals())

c = 2
d = "world!"



print("outside : ")
print(locals())

test1(4,"yes")