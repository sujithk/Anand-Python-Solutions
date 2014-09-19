class bankaccount():
	def __init__(self):
		self.balance=0
	def deposite(self,amount):
		self.balance+=amount
		return self.balance
	def withdrowal(self,amount):
		self.balance-=amount
		return self.balance
a=bankaccount()
b=bankaccount()
print a.deposite(100)
print a.deposite(100)
print a.withdrowal(50)
