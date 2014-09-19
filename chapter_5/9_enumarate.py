def enumarate():
	import itertools
	a=["a","b","c","d"]
	for q,w in itertools.izip(a,range(len(a))):
		print q,w
enumarate()
