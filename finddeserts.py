#Finds gene deserts, top 3% of intergenic distances


import os
from multiprocessing import Pool



f = range(1,23) + ["X"]
def output(a):
	chr = "chr" + str(a)
	file = open(chr + "genes.bed")
	lines = file.readlines()
	for b in range(0,len(lines)-1):
		print "Working on " + str(b) + " out of " + str(len(lines)) + " on " + chr
		first = int(lines[b].split()[2])
		second = int(lines[b+1].split()[1])
		if (second - first < 0): continue
		else:
			st = chr + " " + str(b) + "," + str(b+1)
			dist = str(second-first)
			st += "\t" + dist
			os.system("echo " + st + " >> " + chr + "intergenicdistances.txt")

if __name__ == "__main__":
	pool = Pool(processes=23)
	pool.map(output,f)
	pool.close()
