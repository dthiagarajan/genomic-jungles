#Creates the actual distributions
from random import randint
from multiprocessing import Pool
import os



seqs = {}
seqs1 = {}
enhancers = {}
silencers = {}
eplaced = {}
splaced = {}
minlengths = {}
for a in range(1,23):
	seqs["chr"+str(a)] = []
	seqs1["chr"+str(a)] = []
	enhancers["chr"+str(a)] = []
	silencers["chr"+str(a)] = []
	eplaced["chr"+str(a)] = []
	splaced["chr"+str(a)] = []
	minlengths["chr"+str(a)] = 0
seqs["chrX"] = []
seqs1["chrX"] = []
enhancers["chrX"] = []
silencers["chrX"] = []
eplaced["chrX"] = []
splaced["chrX"] = []

for a in seqs.keys():
	print "Storing enhancers and silencers for " + a
	fe = open(a + "Enhancers.bed")
	fs = open(a + "Silencers.bed")
	le = fe.readlines()
	ls = fs.readlines()
	for b in le:
		enhancers[a].append(b)
	for b in ls:
		silencers[a].append(b)
for a in seqs.keys():
	file = open(a +"distrsequences.txt")
	lin = file.readlines()
	ct = 0
	for b in lin:
		print "Storing for " + str(ct) + " out of " + str(len(lin)) + " in " + a
		ct += 1
		l = b.split()
		l[0] = int(l[0])
		l[1] = int(l[1])
		l[2] = int(l[2])
		seqs[a].append(l)
	print 'Done storing for ' + a
	for i in range(0,1):
		#print "Distributing for silencers in " + a + " for " + str(i) + "th trial"
		temp = seqs[a]
		for count in range(0,len(silencers[a])):
			index = randint(0,len(silencers[a])-1)
			l = int(silencers[a][index].split()[2]) - int(silencers[a][index].split()[1])
			poss = []
			for b in range(0,len(seqs[a])):
				if (int(seqs[a][b][2]) >= l): 
					next = [b,seqs[a][b][2]-l+1]
					poss.append(next)
			if len(poss) == 0: 
				#print 'No possible ones, continuing ' + str(i) + 'th trial in silencers, finished ' + str(count) + "th enhancer of "+ str(len(enhancers[a])) + "enhancers on " + a
				continue
			else: placeind = randint(0,len(poss)-1)
			print "Placing in " + a
			if (poss[placeind][1] > 1):
				nind = randint(seqs[a][poss[placeind][0]][0], seqs[a][poss[placeind][0]][0] + poss[placeind][1])
				print "Adding to splaced in " + a
				print "Silencer: " +  silencers[a][index]
				print "Added at " + str(nind)
				nt = [silencers[a][index], nind]
				splaced[a].append(nt)
				if nind == seqs[a][poss[placeind][0]]:
					lind = seqs[a][poss[placeind][0]][1]
					sind = seqs[a][poss[placeind][0]][0]
					sind += l
					next = [sind,lind,lind-sind+1]
					seqs[a].remove(seqs[a][poss[placeind][0]])
					seqs[a].insert(poss[placeind][0],next)	
				else:
					lind = seqs[a][poss[placeind][0]][1]
					sind = seqs[a][poss[placeind][0]][0]
					seqs[a].remove(seqs[a][poss[placeind][0]])
					firstnext = [sind,nind-1,nind-sind]
					lastnext = [nind+l,lind,lind-nind]
					seqs[a].insert(poss[placeind][0],lastnext)
					seqs[a].insert(poss[placeind][0],firstnext)					
			else:
				print "Adding to splaced in " + a
				ifk = seqs[a][poss[placeind][0]][0]
				nt = [silencers[a][index], ifk]
				splaced[a].append(nt)
				print "Silencer: " +  silencers[a][index]
				print "Added at " + str(seqs[a][poss[placeind][0]][0])
				seqs[a].remove(seqs[a][poss[placeind][0]])
for a in seqs.keys():
	ct = 0
	for b in splaced[a]:
		print "Writing for " + str(ct) + " out of " + str(len(splaced[a])) + " on " + a
		e = b[0]
		start = int(e.split()[1])
		end = int(e.split()[2])
		length = end - start
		command = "echo " + str(b[1]) + " " + str(length) + " >> " + a + "randplaceds.txt"
		os.system(command)
		ct += 1
