balance=0
def deposite(amount):
	global balance
	balance+=amount
	return balance
def wi(amount):
	wit=0
	global balance
	wit-=amount
	return wit
print deposite(100)
print wi(20)
