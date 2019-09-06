#! /usr/bin/python
import sys
from tqdm import tqdm
import pandas as pd
#pd.set_option("display.max_colwidth", 200)
#pd.set_option("display.max_rows", 100)
import radix

rtree = radix.Radix()

# open file and store lines into list
lines1 = [line1.rstrip('\n') for line1 in open(sys.argv[1])]
df = pd.read_csv(sys.argv[2])
lines2 = df['IOC'].values.tolist()

# adding nodes into tree
for line2 in lines2:
	rnode = rtree.add(line2)

matchlist = [] 
# search prefix from tree
for line in tqdm(lines1):
	rnode = rtree.search_covered(line)
	if len(rnode) > 0:
		for i in rnode:
			matchlist.append(i.prefix)

# print matched IOC info 
print(df.query('IOC == %s' % matchlistdf.query('IOC == %s' % matchlist))
#if you want csv output, change last line to like below,
#df.query('IOC == %s' % matchlist).to_csv('result.csv',index=False)
