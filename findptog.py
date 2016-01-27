import os
from multiprocessing import Pool

f = range(1,23) + ["X"]
clusterranges = {}
TSS = {}
for a in f:
	clusterranges["chr"+str(a)] = []
	TSS["chr"+str(a)] = []

file = open("TSS.txt")
lines = file.readlines()
for b in range(0,len(lines)):
	print "Storing TSS for " + str(b) + " out of " + str(len(lines))
	l = lines[b].split()
	if l[0] in TSS.keys():
		s = int(l[2])
		e = int(l[3])
		if l[1] == "+":
			TSS[l[0]].append(s)
		else:
			TSS[l[0]].append(e)


def method(a):
	chr = "chr" + str(a)
	file = open(chr + "clusteredsize1+.bed")
	ct = 0
	lines = file.readlines()
	t = [-1]
	prev = []
	for b in lines:
		print "Storing clusters for " + str(ct) + " out of " + str(len(lines)) + " on " + chr
		ct += 1
		l = b.split()
		if l[0] != "next" and t[0] == -1:
			t[0] = int(l[1])
			prev = l
		if l[0] != "next" and t[0] != -1:
			prev = l
		if l[0] == "next":
			t.append(int(prev[2]))
			clusterranges[chr].append(t)
			avg = (t[0] + t[1])/2
			#Finding first distance, middle of jungle to closest TSS
			min = 100000000
			min1 = 10000000
			rmin = 10000000
			cot=0
			diff = 0
			ndiff = 0
			for c in TSS[chr]:
				print "Working on " + str(cot) + " out of " + str(len(TSS[chr])) + " for the " + str(ct) + " cluster out of " + str(len(lines)) + "  on " + chr
				cot += 1
				diff = avg - c
				mult = 0
				if diff < 0: mult = diff * -1
				else: mult = diff
				
				if (mult < min): 
					min = mult
					rmin = diff
				ndiff = 0
				if c < t[0]: ndiff = t[0]-c
				elif c == t[0] or c == t[1]: ndiff = 0
				else: ndiff = c - t[1]
				
				if ndiff < min1: min1 = ndiff
			os.system("echo " + str(rmin) + " >> midjgTSSdist1+.txt")
			os.system("echo " + str(ndiff) + " >> edgejgTSSmindist1+.txt")
			t = [-1]
			prev = []

if __name__ == "__main__":
	pool = Pool(processes = 23)
	pool.map(method,f)
	pool.close()

