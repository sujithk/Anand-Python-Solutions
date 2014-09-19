# Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.
def split(filename,no_lines):
	m=readfiles(filename)
	n=totallines(filename)
	y=n/no_lines
	print y
	b=0
	i=0
	while(y>b):
		mn=["a","b","c","d"]
		writelines(m,b,mn,i,no_lines)
		print "no_lines:%d"%no_lines
		b+=1
		i=i+no_lines
def readfiles(filename):
	x=[]
	we=open(filename,"r")
	for q in we:
		x.append(q)
	return x

def totallines(filename):
	a=open(filename)
	t=len(a.readlines())
	return t
def writelines(m,b,mn,i,no_lines):
	kl=open(mn[b],"w")
	print m[i:i+no_lines]
	for qwe in m[i:i+no_lines]:
		kl.write(qwe+'\n')
	kl.close() 
		
split("sample.txt",2)		
