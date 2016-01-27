seqs = {}
enhancers = {}
silencers = {}
minelength = {}
minslength = {}
for a in range(1,23):
	seqs["chr"+str(a)] = []
	enhancers["chr"+str(a)] = []
	silencers["chr"+str(a)] = []
	minelength["chr"+str(a)] = 0
	minslength["chr"+str(a)] = 0
seqs["chrX"] = []
enhancers["chrX"] = []
silencers["chrX"] = []
minelength["chrX"] = 0
minslength["chrX"] = 0
#In all these methods, a is the chromosome which is being worked on


for a in seqs.keys():
	print "Storing enhancers and silencers for " + a
	fe = open(a + "Enhancers.bed")
	fs = open(a + "Silencers.bed")
	le = fe.readlines()
	ls = fs.readlines()
	mine = 19999999
	mins = 19999999
	for b in le:
		print b
		enhancers[a].append(b)
		print 'Added to enhancers on ' + a
		print b.split()[0]
		print b.split()[1]
		print b.split()[2]
		nlen = int(b.split()[3]) - int(b.split()[2])
		if nlen < mine: mine = nlen
	minelength[a] = mine
	print 'Updated min length for enhancers on ' + a
	for b in ls:
		print b
		silencers[a].append(b)
		print 'Added to silencers on ' + a
		nlen = int(b.split()[3]) - int(b.split()[2])
		if nlen < mins: mins = nlen
	minslength[a] = mins
	print 'Updated min length for enhancers on ' + a

