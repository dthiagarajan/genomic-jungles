import os
files = ["allenhancers.bed","allsilencers.bed"]
b = range(1,23) + ["X"]
for a in files:
	print a
	for c in b:
		s = "chr" + str(c)
		print s
		command = "cat " + a + ''' | grep -P "''' + s + '''\t" > ''' + s 
		print command
		if "enhancer" in a:
			os.system("cat " + a + ''' | grep -P "''' + s + '''\t" > ''' + s + "Enhancers.bed")
		else:
			os.system("cat " + a + ''' | grep -P "''' + s + '''\t" > ''' + s  + "Silencers.bed")
			
