#Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.
files=["sample.txt","sample2.txt"]
k=[]
def readfiles(files):
	for f in files:
		for q in open(f):
			 k.append(q)
	return k
u=readfiles(files)
def select(u):
	for e in u:
		if len(e)>12:
			print e
		#print e
select(u)	
