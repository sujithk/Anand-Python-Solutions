def grep(s,i):
	for line in open(s):
		if i in line:
			print line

grep("17_she.txt","seashore")
