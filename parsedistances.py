f = range(1,23) + ["X"]
import os
for a in f:
	chr = "chr" + str(a)
	print chr
	command = "cat " + chr + "randplaceds.txt | sort -k1,2n > " + chr + "sortedrandplaceds.txt"
	os.system(command)

for a in f:
	chr = "chr"+str(a)
	print a
	fname = chr + "sortedrandplaceds.txt"
	file = open(fname)
	lines = file.readlines()
	for b in range(0,len(lines)-1):
		print str(b) + " out of " + str(len(lines))
		s1 = lines[b].split()
		s2 = lines[b+1].split()
		dist = int(s2[0]) - int(s1[1])-int(s1[0])
		command = "echo " + str(dist) + " >> alldistss.txt"
		os.system(command)

f = open("alldistss.txt")
lines = f.readlines()
ct = 0
for a in lines:
	ct += 1
	print str(ct) + " out of " + str(len(lines))
	if (abs(int(a)) < 100): continue
	else:
		command = "echo " + str(abs(int(a))) + " >> alldistancess.txt"
		os.system(command)
