#Write a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs.

def listtime():
        import os
        import time
        a= os.listdir('.')
        for q in a:
                t=os.path.getsize(q)
                p=os.path.getmtime(q)
                print q,t,p
listtime()

