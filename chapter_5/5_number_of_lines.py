#Write a function to compute the total number of lines of code in all python files in the specified directory recursively.
import re
import os
n=[]
def listallfiles():
        q=os.listdir(".")
        return q
def search_python_files(l):
        for u in l:
                y=re.match(r'.\w*.py$',u)
                if y:
			p=readfiles(u)
			n.append(p)
		
        print "The total count of python lines:",sum(n)
def readfiles(k):
	print k
	p=len(open(k).readlines())
	print p
	return p
l=listallfiles()
search_python_files(l)
