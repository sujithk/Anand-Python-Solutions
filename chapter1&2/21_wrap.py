a=open('17_she.txt','r')
b=a.readlines()
def wrap(a,l):
	for q in b:
		n=0
		for v in b:
			i=v[n:n+l]
			n=n+l
			print i

wrap(a,30)


