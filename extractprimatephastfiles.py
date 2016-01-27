import os
for a in range(1,23):
        os.system('wget http://hgdownload-test.cse.ucsc.edu/goldenPath/hg19/phastCons46way/primates/chr' + str(a) + '.phastCons46way.primates.wigFix.gz')
os.system('wget http://hgdownload-test.cse.ucsc.edu/goldenPath/hg19/phastCons46way/primates/chrX.phastCons46way.primates.wigFix.gz')

