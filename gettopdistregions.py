file = open("alldistances.txt")
lines = file.readlines()
import os



imax = 0
ivalmax = -1
maxlines = []
for i in range(0,1610):
	print "Finding " + str(i) + " trial"
	for a in range(0,len(lines)):
		#print "On " + str(a) + " line"
		l = lines[a].split()
		if int(l[2]) >= ivalmax:
			imax = a
			ivalmax = int(l[2])
	command = "echo " + lines[imax][:-1] + " >> maxinterdists.txt"
	print command
	os.system(command)
	lines.remove(lines[imax])
	imax = 0
	ivalmax = -1
		
	
