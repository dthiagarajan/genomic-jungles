cut = 570
import os
from multiprocessing import Pool
a = range(1,23)+["X"]
files = []
clusters = {}
for b in a:
	chr = "chr"+str(b)
	clusters[chr] = []
	files.append(chr)

#for file in files:
def cluster(file):
	f = open(file + "enhancers.bed")
	lines = f.readlines()
	next = []
	for a in range(0,len(lines)):
		print "clustering on " + str(a) + " out of " + str(len(lines)) + " on " + file
		if (a==0):
			next.append(lines[0].split())
			continue
		on = lines[a].split()
		if (len(next) == 0): 
			next.append(on)
			continue
		pend = int(next[-1][2])
		ostart = int(on[1])
		if (ostart-pend < cut): next.append(on)
		else:
			clusters[file].append(next)
			next = []
	ct = 0
	f = open(file + "silencers.bed")
	lines = f.readlines()
	for a in range(0,len(lines)):
		print "finding relative distance of silencers on " + str(a) + " out of " +  str(len(lines)) + " on " + file
		start = int(lines[a].split()[1])
		end = int(lines[a].split()[2])
		print start
		print end
		mindist = 1000000000
		pastloc = False
		ct = 0
		for b in clusters[file]:
			if len(b) == 1: continue
			print "Finding mindist for " + str(ct) + " out of " + str(len(clusters[file])) + " on " + str(a) + "silencer on " + file
			ct+=1
			if (pastloc): continue
			else: pastloc = False

			cstart = int(b[0][1])
			cend = int(b[-1][2])
			dist = 0
			if end <= cstart: dist = cstart - end
			if start >= cend: 
				pastloc = True
				dist = start - cend
			if (dist < mindist): mindist = dist
		os.system("echo " + str(mindist) + " >> relativesilencerdists1.txt")
						
"""
	for a in clusters[file]:
		ct += 1
		print "Finding lengths and sizes and interdistances for " + str(ct) + " out of " + str(len(clusters[file])) + " on " + str(file)
		size = len(a)
		
		if (size == 1): continue
		
		length = int(a[-1][2]) - int(a[0][1])
		os.system("echo " + str(size) + " >> clustersizes+1.txt")
		os.system("echo " + str(length) + " >> clusterlengths+1.txt")
		
		for b in range(0,len(a)-1):
			first = a[b]
			second = a[b+1]
			di = int(second[1]) - int(first[2])
			os.system("echo " + str(abs(int(di))) + " >> intraclusterdistances+1.txt")
		
		for b in a:
			print "Writing for " + str(file)
			st = ""
			for c in b:
				st += c
				st += " "
			os.system("echo " + st + " >> " + file + "clusteredsize1+.bed")
		os.system("echo next >> " + file + "clusteredsize1+.bed")
	for a in range(0,len(clusters[file])-1):
		print "Finding interclusterdistance for " + str(a) + " out of " + str(len(clusters[file])) + " on " + str(file)
		first = clusters[file][a]
		second = clusters[file][a+1]
		dist = int(second[0][1])-int(first[-1][2])
		os.system("echo " + str(dist) + " >> interclusterdistances+1.txt")
"""
if __name__ == "__main__":
	pool = Pool(processes=23)
	pool.map(cluster,files)
	pool.close()
