def map(f,b):
	return [f(x) for x in b]
def f(x):
	return x*x

print map(f,range(5))	
