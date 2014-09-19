u=0
def dirttyy(a):

	import os

	for q in os.listdir(a):
#		print q
		if os.path.isdir(q):
			print q+'/'
			print q
			global u
			u+=1
			dirttyy(q)
		else:
#			print u
			print '| |'* u+'--'+q	
dirttyy('/home/najeeb/recursive/book/anandh_python/chapter_6')
