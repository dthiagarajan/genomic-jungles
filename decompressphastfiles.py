import os
for a in range(1,23):
	os.system('gunzip chr' + str(a) + '.phastCons46way.placental.wigFix.gz')
	os.system('gunzip chr' + str(a) + '.phastCons46way.primates.wigFix.gz')
