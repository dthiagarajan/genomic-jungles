e = "allenhancers_sorted_filtered_merged_filtered_merged_filtered.bed"
el = "elengths.txt"
s = "allsilencers_sorted_filtered_merged_filtered_merged_filtered.bed"
sl = "slengths.txt"
files = [e,s]
import os
for a in files:
	f = open(a)
	lines = f.readlines()
	ct = 0
	for b in lines:
		ct += 1
		print "counting for " + str(ct) + " out of " + str(len(lines))
		l = b.split()
		length = int(l[2]) - int(l[1])
		if length>3000: 
			print 'here'
			continue
		if (a==e):
			os.system("echo " + str(length) + " >> " + el)
		else:
			os.system("echo " + str(length) + " >> " + sl)
