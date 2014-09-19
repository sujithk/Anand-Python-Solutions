def main(pattern,filename):
	readfiles(filename)
	grep(pattern,filename)
def readfiles(filename):
	for o in open(filename):
		print  o	
def grep(pattern,filename):
	for o in open(filename):
		if pattern in o:
			print o
main("as","sample.txt")
