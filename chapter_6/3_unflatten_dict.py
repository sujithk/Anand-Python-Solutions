#Write a function unflatten_dict to do reverse of flatten_dict.
a={'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
def unflatten_dict(a,result=None):
	if result==None:
		result={}
	m=[]
	n=[]
	kl={}
	er=[]
	z={}
	for q in a:
		if '.' in q:
#			print q
			n.append(a[q])
			m.append(q.split('.'))
#			print m,n
			v=m[0][0]
#			print v
			p=0
			for s,j in m:
				kl[j]=n[p]
				p+=1
#			print kl
			z[v]=kl
			unflatten_dict(z,result)
			print z
		else:
			result[q]=a[q]
			
	return result		
print unflatten_dict(a)
