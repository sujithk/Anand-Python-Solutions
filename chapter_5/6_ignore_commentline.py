import re
import os
n=[]
mn=open("withoutcomment.txt","w")
def listallfiles():
        q=os.listdir(".")
        return q
def search_python_files(l):
        for u in l:
                y=re.match(r'.\w*.py$',u)
                if y:
                        p=readfiles(u)
	mn.close()	
	o=calculate(p)

        print "The total count of python lines:",o
def readfiles(k):
        print k
	qw=open(k).readlines()
	for e in qw:
		if not (e.startswith("#")|e.startswith("'''")):
			mn.write(e)
def calculate(p):
	mn=open("withoutcomment.txt","r")
	p=len(mn.readlines())
	mn.close()
        print p
        return p
l=listallfiles()
search_python_files(l)

