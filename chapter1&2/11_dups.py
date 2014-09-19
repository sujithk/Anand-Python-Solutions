def dups(a):
	b=[]
	c=[]
	for v in a:
		if a.count(v)>1:
			b.append(v)
	print b
	for q in b:
		if q not in c:
			c.append(q)
	print c

dups([1,2,1,3,2,5])
