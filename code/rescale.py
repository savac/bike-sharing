"""
Rescale a submission
"""

import csv
from numpy import float, sqrt, log

# File to rescale
input_file = '../data/sub2.csv'
output_file = '../data/sub2_rescaled.csv'
field_names = ['datetime', 'count']

# Constants
score_all_zeros = 4.76189
n_S = 6493 # Number observations in the test file
n_s = 0; # Number of observations in input_file (not used)

S = n_S * (score_all_zeros**2) # Sum of ln(1+a_i)²
s = 0.0

# Compute the current sum of rows
with open(input_file, 'r') as csvfile:
	csvreader = csv.DictReader(csvfile)
	
	for row in csvreader:
		n_s += 1
		s += log(1.0 + float(row[field_names[1]])) ** 2

# Rescale all numbers
with open(input_file, 'r') as csvfile:
	csvreader = csv.DictReader(csvfile)
	
	with open(output_file, 'w', newline='') as output_csvfile:
		csvwriter = csv.DictWriter(output_csvfile, fieldnames=field_names)
		
		csvwriter.writeheader()
		for row in csvreader:
			p_i = float(row[field_names[1]])
			p_i = (1.0 + p_i) ** sqrt(S / s) - 1.0 # rescale here
			csvwriter.writerow({field_names[0]:row[field_names[0]], field_names[1]:p_i})
