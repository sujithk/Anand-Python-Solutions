a=open("sample.txt","r")
j=1
for q in a.readlines():
	if j>len(a.readlines()):
		#if j<len(open("sample.txt").readlines()):
		print len(a.readlines())
		print j
		print q
		j-=1     
	else:
		j+=1                   
