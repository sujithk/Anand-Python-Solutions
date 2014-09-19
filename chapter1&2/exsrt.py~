def exsrt(a):
	p=[]
	r=[]
	s=[]
	t=[]
	for q in a:
		p.append(q.split("."))
	i=0
	for v in p:
		r.append(p[i][0])
		s.append(p[i][1])
		i=i+1	
		z=zip(s,r)
		z.sort()
	j=0
	for x in z:
		t.append(".".join([z[j][1],z[j][0]]))
		j=j+1
	return t	
		
		

print exsrt(['a.c','a.py','b.py','bar.txt','foo.txt','x.c'])
