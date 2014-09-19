def cum(a):
	s=0
	b=[]
	for v in a:
		s=s+v
		b.append(s)
	print b

cum([1,2,3])
