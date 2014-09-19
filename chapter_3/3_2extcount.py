import os
def extcount(dir):
	dict={}
	#filenames=os.listdir(dir)
	filenames=os.listdir(os.path.abspath(dir))
	for filename in filenames:
		dict[filename.split('.')[0]]=dict.get(filename.split)
	return dict

print extcount('/home/sujith/cp/rv/anand/chap1,2')
		
	
