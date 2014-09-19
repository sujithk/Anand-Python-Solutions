def enu(p):
	s=[]
	for v in p:
		q=p.index(v)
		s.append(q)
	return zip(s,p)


print enu(["a","b","c"])
