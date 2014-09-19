def head(s):
	a=[]
	for line in open(s):
		a.append(line)
	t=a[0:3]
	for i in t:
		print i

head("17_she.txt")
