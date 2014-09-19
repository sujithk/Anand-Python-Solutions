#mplement a function izip that works like itertools.izip.
def izip():
	a=["a","b","c"]
	b=[0,1,2]
	#print [(x,y) for x in a for y in b if a.index(x)==b.index(y)]
	for x in a:
		for y in b:
			if a.index(x)==b.index(y):
				print x,y
izip()

