def match():
	import re
	strr='asian paints'
	r=raw_input("enter searching word:")
	matchh=re.search(r,strr)
	if matchh:
		print 'found',matchh.group()
	else:
		print 'not found'
match()
