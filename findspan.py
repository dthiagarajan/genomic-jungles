from multiprocessing import Pool
import os
f = range(1,23) + ["X"]
genelociranges = {}
clusterranges = {}
percs = {}
clusterlens = {}
for a in f:
	chr = "chr" + str(a)
	genelociranges[chr] = []
	clusterranges[chr] = []
	percs[chr] = 0
	clusterlens[chr] = 0
	
def methodall(a):
	chr = "chr" + str(a)
	file = open(chr + "genes.bed")
	lines = file.readlines()
	ct = 0
	for l in lines:
		print "Working on " + str(ct) + " out of " + str(len(lines)) + " on " + chr
		ct += 1
		chr = l.split()[0]
		s = int(l.split()[1])
		e = int(l.split()[2])
		n = [s,e]
		genelociranges[chr].append(n)
	chr = "chr" + str(a)
	file = open(chr + "clustered.bed")
	ct = 0
	lines = file.readlines()
	t = [-1]
	prev = ""
	t = [-1]
	prev = []
	for b in lines:
		print "Working on getting span for " + str(ct) + " out of " + str(len(lines)) + " on " + chr
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
			t = [-1]
			prev = []
	oct = 0
	clusterlens[chr] = len(clusterranges[chr])
	for b in clusterranges[chr]:
		scluster = set(range(b[0],b[1]))
		overlapcount = 0
		for c in genelociranges[chr]:
			if (overlapcount > 1):
				oct += 1
				break
			if b[1] < c[0]: continue
			if c[1] < b[0]: break
			sn = set(range(c[0],c[1]))
			if len(scluster & sn) > 0: overlapcount += 1
		if (overlapcount == 0):
			min = 1000000000
			for c in genelociranges[chr]:
				if b[1] < c[0]:
					if min > c[0]-b[1]: min = c[0]-b[1]
				if c[1] < b[0]:
					if min > b[0]-c[1]: min = b[0]-c[1]
			os.system("echo " + str(min) + " >> " + chr + "proximitytogenes.txt")
	percs[chr] = oct * 1.0
	frac = percs[chr] / clusterlens[chr]
	#os.system("echo " + str(percs[chr]) + " " + str(clusterlens[chr]) + " >> " + chr + "spanpercentage.bed")
		
if __name__ == "__main__":
	pool = Pool(processes=23)
	pool.map(methodall,f)
	pool.close()
