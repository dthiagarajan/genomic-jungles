#Creates distribution of random distances over several trials
from multiprocessing import Pool
seqs = {}
lengths = {}
for a in range (1,23):
	seqs["chr" + str(a)] = []
seqs["chrX"] = []

import os

def store(a):
	f = open(a + ".fa.masked")
	lines = f.readlines()
	print "Storing for " + a
	lengths[a] = len(lines)*len(lines[1])
	prlen = 0
	first = -1
	last = -1
	for b in range(0,len(lines)):
		if (b==0):continue
		lines[b] = lines[b].split()[0]
		print "Looking at " + str(b) + " line out of " + str(len(lines)) + " lines in " + a 
		for c in range(0,len(lines[b])):
			if (lines[b][c] != "N" and first == -1):
				first = c + prlen
				continue
			if (lines[b][c] == "N" and first != -1):
				st = str(first) + " " + str(last)
				os.system('echo ' + st + " >> " + a + "codingseqs.txt")
				first = -1
				last = -1
				continue
			if (lines[b][c] != "N" and first != -1):
				last = c + prlen
				continue
		prlen+=len(lines[b])
	print "Done storing noncoding sequences"

if __name__ == '__main__':
	pool = Pool(processes=23)
	pool.map(store,seqs.keys())
	pool.close()

