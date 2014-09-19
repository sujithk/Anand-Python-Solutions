#Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces and special characters are replaced by a hyphen, typically used to create blog post URL from post title. It should also make sure there are no more than one hyphen in any place and there are no hyphens at the biginning and end of the slug.
def make_slug():
	import re
	strr='hello world!'
	r=re.sub(r'\w\+([\s-]+)','-',strr)
	print r
	x=re.search(r'(.*)-(\w*)',r)
	if x:
		print 'matching',x.group()
	else:
		print 'not matching'
make_slug()
