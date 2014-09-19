#Write a function tree_reverse to reverse elements of a nested-list recursively.
def tree_reversal(a,result=None):
	if result==None:
		result=[]
	h=[]
	for q in a:
		if isinstance(q,list):
			print q
			n=q[ : :-1]
			print n
#			tree_reversal(n,result)
			result.append(n)		
		else:	
			result.append(q)
	re=result[ : :-1]
	return re
print tree_reversal([[1, 2], 3,[4, 5], 6])
