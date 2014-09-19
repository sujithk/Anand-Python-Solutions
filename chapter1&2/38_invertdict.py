def inverdict(d):
	dict={}
	for k,v in d.items():
		dict[v]=k
	return dict

print inverdict({'x':1,'y':2,'z':3})
