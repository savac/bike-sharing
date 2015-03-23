import numpy as np

test_file = '../data/test.txt'
pred_file = '../data/predictions.txt'

pred_file = open(pred_file,'rb')
test_file = open(test_file,'rb')

r = 0
n = 0
while True:
	pred_line = pred_file.readline()
	test_line = test_file.readline()
	if test_line == "":
		break
		
	test_line = test_line.split(' ')
	trueval = float(test_line[0])
	predval = float(pred_line.strip('\n'))
	
	n += 1
	r += (np.log(predval+1) - np.log(trueval+1))**2
print 'EVAL SCORE = %f' %((r/n)**0.5)

	
