import random
import sys

in_file = '../data/train.txt' # Source file (CSV)
out_file = '../data/train.txt' # File for VW (TXT)

if len(sys.argv) >= 3:
	in_file = sys.argv[1]
	out_file = sys.argv[2]

with open(in_file,'r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open(out_file,'w') as target:
    for _, line in data:
        target.write( line )
