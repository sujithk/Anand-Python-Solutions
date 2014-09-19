def readfiles(a):
	b=open(a)
	for q in b:
		print q
#		grep(pattern,filename)
readfiles("sample.txt")
def grep(pattern,filename):
	for q in open(filename):
		if pattern in q:
			print q
grep("as","sample.txt")
