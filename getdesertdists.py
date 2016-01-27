import os
from multiprocessing import Pool


distart = {}
diend = {}
dimid = {}
clusterstart = {}
clusterend = {}
clustermid = {}
for a in range(1,23):
	chr = "chr" + str(a)
	distart[chr] = []
	diend[chr] = []
	dimid[chr] = []
	clusterstart[chr] = []
	clusterend[chr] = []
	clustermid[chr] = []
distart["chrX"] = []
diend["chrX"] = []
dimid["chrX"] = []
clusterstart["chrX"] = []
clusterend["chrX"] = []
clustermid["chrX"] = []


def readclusters(a):
	f = open(a+"clusteredsize1+.bed")
	lines = f.readlines()
	first = -1
	last = -1
	for b in range(0,len(lines)):
		print "Storing clusters, on line " + str(b) + " out of " + str(len(lines)) + " on " + a
		if "next" in lines[b]:
			last = int(lines[b-1].split()[2])
			clusterstart[a].append(first)
			clusterend[a].append(last)
			clustermid[a].append((first+last)/2)
			first = -1
			last = -1
		else:
			if first == -1: first = int(lines[b].split()[1])
			else: continue
				

def readdeserts(a):
	starts = open(a + "genedesertstart.txt")
	ends = open(a + "genedesertend.txt")
	mids = open(a + "genedesertmid.txt")
	slines = starts.readlines()
	elines = ends.readlines()
	mlines = mids.readlines()
	for b in range(0,len(slines)):
		print "Storing desert stuff: " + str(b) + " out of " + str(len(slines))
		distart[a].append(int(mlines[b]))
		diend[a].append(int(mlines[b]))
		dimid[a].append(int(mlines[b]))

#def finddists(a):
	for ct in range(0,len(clusterend[a])):
		print "Working on " + str(ct) + " out of " + str(len(clusterend[a])) + " on " + a
		cstart = clusterstart[a][ct]
		cend = clusterend[a][ct]
		cmid = clustermid[a][ct]
		min = 1000000000
		imin = 0
		lmin = "-"
		check = False
		for b in range(0,len(diend[a])):
			#print "Finding closest desert region: working on " + str(b) + " out of " + str(len(diend[a])) + " on " + a
			if (check): break
			dstart = distart[a][b]
			dend = diend[a][b]
			if (dend < cstart):
				nl = cstart-dend
				if nl < min:
					min = nl
					imin = b
					lmin = "end"
			if (dstart > cend):
				check = True
				nl = dstart - cend
				if nl < min:
					min = nl
					imin = b
					lmin + "start"
		os.system("echo " + str(min) + " >> clusterdesertmindists1.txt")
		if lmin == "end":
			dmid = dimid[a][imin]
			dend = diend[a][imin]
			os.system("echo " + str(cmid-dmid) + " >> clusterdesertmidmiddists1.txt")
			if (cstart-dmid) > 0: os.system("echo " + str(cstart-dmid) + " >> clusterdesertmidclosestdists1.txt")
			if (cmid-dend) > 0: os.system("echo " + str(cmid-dend) + " >> clusterdesertclosestmiddists1.txt")
			
		else:
			dmid = dimid[a][imin]
			dstart = distart[a][imin]
			os.system("echo " + str(dmid-cmid) + " >> clusterdesertmidmiddists1.txt")
			if (dstart-cmid)>0: os.system("echo " + str(dstart-cmid) + " >> clusterdesertmidclosestdists1.txt")
			if (dmid-cend)>0: os.system("echo " + str(dmid-cend) + " >> clusterdesertclosestmiddists1.txt")
			



if __name__ == "__main__":
	pool = Pool(processes = 23)
	pool.map(readclusters,diend.keys())
	pool.map(readdeserts,diend.keys())
	#pool.map(finddists,diend.keys())
	pool.close()
