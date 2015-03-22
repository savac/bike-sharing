"""
Convert to the CSV format for submission
Feel free to modify if there is mistakes.
"""

pred_file = '../data/predictions.txt' # File from VW (TXT)
csv_file = '../data/test.csv'

import sys

if len(sys.argv) >= 2:
	txt_file = sys.argv[1]
	
pred_file = open(pred_file,'rb')
csv_file = open(csv_file,'rb')


submission_file = open('../data/submission.csv','w')
submission_file.write('datetime,count\n') # Write header

csv_file.readline() # skip one line
while True:
	csv_line = csv_file.readline()
	pred_line = pred_file.readline()
	if csv_line == "":
		break
	csv_line = csv_line.split(',')

	submission_file.write(csv_line[0]+','+pred_line)

	

