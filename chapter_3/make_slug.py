def make_slug(a):
	import re
	lis=re.findall(r'(\w+)',a)
	print "-".join(lis)
make_slug("-----hello worldaaaaaa fffffff")
