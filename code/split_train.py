import sys

in_file = '../data/train.txt'
out_file1 = '../data/train.txt'
out_file2 = '../data/test.txt'
frac = 0.9

if len(sys.argv) >= 5:
	in_file = sys.argv[1]
	out_file1 = sys.argv[2]
	out_file2 = sys.argv[3]
	frac = float(sys.argv[4])

in_file = open(in_file, 'rb')
mylist = in_file.readlines()
print len(mylist)
in_file.close()

out_file1 = open(out_file1, 'w')
for i in range(0, int(round(len(mylist)*0.9))):
	out_file1.write(mylist[i])
	
out_file2 = open(out_file2, 'w')
for i in range(int(round(len(mylist)*0.9)), len(mylist)):
	out_file2.write(mylist[i])
