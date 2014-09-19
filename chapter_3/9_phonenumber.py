#Write a regular expression to validate a phone number.
def phone():
	import re
	phone='9895123456'
	q=re.match(r'\d\d\d\d\d\d\d\d\d\d',phone)
	if q:
		print 'phone number matching:',q.group()
	else:
		print "not matching"
phone()

