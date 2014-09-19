def product(x,n):
	if x==0:
		return 0
	elif n==0:
		return 0
	else:
		return x+product(x,n-1)
print product(5,4)
