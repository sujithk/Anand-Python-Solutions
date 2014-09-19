def lensort(a):
	d=[]
	for v in sorted(a, key=len):
		d.append(v)
	print d

lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])

