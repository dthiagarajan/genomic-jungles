f = open("files.txt")
lines = f.readlines()
files = []
for a in lines:
	files.append(a.split()[0][16:len(a.split()[0])-7])
cats = ["Strong_Enhancers", "Weak_Enhancers", "Represseds"]

import os
for a in files:
	print a 
	for c in cats:
		print c 
		os.system("cat " + a + "_" + c + ".bed.ECRfilter | sort -k1,1 -k2,2n > " + a + "_" + c + "_sorted.bed")

