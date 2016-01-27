import os
from multiprocessing import Pool
files = []
for a in range(1,23):
	s = "chr" + str(a)
	files.append(s)
files.append("chrX")

def ncluster(a):
	os.system("cat " + a + "all.bed | grep Enhancer >> " + a + "enhancers.bed") 
	os.system("cat " + a + "all.bed | grep Silencer >> " + a + "silencers.bed")
	print "Done separating for " + a





if __name__ == "__main__":
	pool = Pool()
	pool.map(ncluster,files)
	pool.close()
