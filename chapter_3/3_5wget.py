import os
#import urllib
url=("http://docs.python.org/tutorial/")
def wget(url):
	if url[-1]=='/':
		basename='index.html'
	else:
		basename=url.split('/')[-1]

	print 'saving',url,'as',basename


wget(url)
	
