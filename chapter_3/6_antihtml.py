# Write a program antihtml.py that takes a URL as argument, downloads the html from web and print it after stripping html tags.
a='<p>http docs.python.org tutorial interpreter.html</p>'
def antihtml(a):
	import os
	import re
	import urllib
#	response=urllib.urlopen(a)
#	print response.headers
	e=re.sub(r'<[^>]+>','',a)
#	print e
	t=re.search(r'\w*.*',e)
	w=re.findall(r'\w*',e)
	for q in w:
		print q

antihtml(a)
