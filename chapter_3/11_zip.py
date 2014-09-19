def zip():
	import zipfile
	z=['zxc.zip','jkl.txt','yui.txt']
	for q in z:
		j=zipfile.is_zipfile(q)
		print j
zip()
