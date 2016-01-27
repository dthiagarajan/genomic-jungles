import os

f = open("files.txt")
lines = f.readlines()
files = []
for a in lines:
	files.append(a.split()[0][16:len(a.split()[0])-7])
cats = ["Strong_Enhancers", "Weak_Enhancers", "Represseds"]

files = ["allenhancers","allsilencers"]

for a in files:
	file = open(a+"_sorted_filtered_merged_filtered_merged.bed")
	lines = file.readlines()
	ct = 0
	for b in lines:
		ct += 1
		print "Counting " + str(ct) + " out of " + str(len(lines)) + " in " + a
		l = b.split()
		start = int(l[1])
		end = int(l[2])
		print end - start
		if (end - start <= 3000):
			st = l[0] + " " + l[1] + " " + l[2]
			command = 'echo ' + st + " >> "
			if "Enhancers" in a:
				os.system(command+a+"_sorted_filtered_merged_filtered_merged_filtered.bed")
			else:
				os.system(command+a+"_sorted_filtered_merged_filtered_merged_filtered.bed")
		else: continue


