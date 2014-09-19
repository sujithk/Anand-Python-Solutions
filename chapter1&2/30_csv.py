a='parse.txt'
a=open(a).readlines()
b=[]
def csv(a):
	for v in a:
		a=v.split(",")
		b.append(a)
	return b


print csv(a)
		
