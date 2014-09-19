#Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.
def flatten_dict(a,result=None):
	if result==None:
		result={}
	for z in a:
		if isinstance(a[z],dict):
			v=a[z].items()
			l=0
			kl=[]
			res={}
			for d in v:
				kl.append(".".join([z,v[l][0]]))
				l+=1
			hj=a[z].values()
			s=[(x,y) for x in kl for y in hj if kl.index(x)==hj.index(y)]
			
			for u,v in s :
				res[u]=v
			flatten_dict(res,result)
		else:
			result[z]=a[z]
	return result
print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})	
