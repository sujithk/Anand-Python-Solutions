import stat
import os
#dir=sys.argv[1]
def listoffiles(dir):
	#filenames=os.listdir(os.path.abspath(dir))
	filenames=os.listdir(dir)
	#return filenames
	for filename in filenames:
		print  filename,' ',len(filename),' ',os.stat(os.path.abspath(os.path.join))


listoffiles('/home/sujith/cp/rv/anand/chap1,2')
