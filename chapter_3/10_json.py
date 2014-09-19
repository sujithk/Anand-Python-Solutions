def jsonn():
	import urllib
	response=urllib.urlopen("http://httpbin.org/get")
	print response.headers
jsonn()
