#Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.
import os
def findfiles():
	q=os.listdir(".")
	for j in  q:
		print os.path.abspath(j)
	
findfiles()
