#Finds distances between enhancers and silencers, respectively
#Using grep to get the chr first, then finding distances

chrs = range(1,23) + ['X']
ef = "allenhancers_sorted_filtered_merged_filtered_merged_filtered.bed"
efn = "alldistances.txt"
sf = 'allsilencers_sorted_filtered_merged_filtered_merged_filtered.bed'
sfn = "alldistancess.txt"
files = [ef,sf]
import os
for a in files:
	print a
	f = open(a)
	lines = f.readlines()
	ct = 0
	for b in range(0,len(lines)-1):
		ct += 1
		print "Counting for " + str(ct) + " out of " + str(len(lines))
		if (lines[b].split()[0] != lines[b+1].split()[0]): continue
		c1 = int(lines[b].split()[2])
		c2 = int(lines[b+1].split()[1])
		dist = c2-c1
		print dist
		if (a == ef):
			os.system("echo " + str(dist) + " >> " + efn)
		else:
			os.system("echo " + str(dist) + " >> " + sfn)
