def rev(a):
	w=1
	b=[]
	for v in a:
		b.append(a[-w])
		w=w+1
	return b

print rev([1,2,3,4])
