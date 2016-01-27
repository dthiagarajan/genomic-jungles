import os
for a in range(1,23):
	os.system('wget http://hgdownload-test.cse.ucsc.edu/goldenPath/hg19/phastCons46way/placentalMammals/chr' + str(a) + '.phastCons46way.placental.wigFix.gz')
os.system('wget http://hgdownload-test.cse.ucsc.edu/goldenPath/hg19/phastCons46way/placentalMammals/chrX.phastCons46way.placental.wigFix.gz')

