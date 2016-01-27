end = "_sorted_filtered_merged_filtered.bed"
cats = ["Strong_Enhancers","Weak_Enhancers","Represseds"]
f = open("files.txt")
lines = f.readlines()
files = []
for a in lines:
	files.append(a.split()[0][16:len(a.split()[0])-7])
import os
files = "allenhancers","allsilencers"
for a in files:
	print a
	fname = a + end
	fi = open(fname)
	os.system("cat " + fname + ''' | awk '{print$1"\t"$2"\t"$3}' > ''' + a + "_sorted_filtered_merged_filtered_tabbed.bed")
	os.system("bedtools merge -i " + a + "_sorted_filtered_merged_filtered_tabbed.bed > " + a + "_sorted_filtered_merged_filtered_merged.bed") 	
