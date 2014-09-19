#rite a function to compute the number of python files (.py extension) in a specified directory recursively.
import re
import os
def listallfiles():
	q=os.listdir(".")
	return q
def search_python_files(l):
	count=0
	for u in l:
		print u
		y=re.match(r'.\w*.py$',u)
		if y:
			count+=1
	print "The total count of python files:",count
l=listallfiles()
search_python_files(l)
