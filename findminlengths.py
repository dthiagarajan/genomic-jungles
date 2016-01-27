files = range(1,23) + ["X"]
fil = ["Enhancers.bed","Silencers.bed"]
import os
for a in files:
	minlength = 10000000000000000
	for b in fil:
		fname = "chr"+str(a)+b
		print fname
		f = open(fname)
		lines = f.readlines()
		for c in lines:
			end = int(c.split()[2])
			start = int(c.split()[1])
			length = end-start
			if length<minlength: minlength = length
	st = "chr"+str(a)+" " + str(minlength)
	os.system("echo " + st + " >> minlengths.txt")
