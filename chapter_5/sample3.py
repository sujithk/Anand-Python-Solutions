def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            print line
readfiles("sample.txt","sample2.txt")
