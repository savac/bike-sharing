"""
Code to parse the tsv file, create features and output the txt file for VW

Feel free to modify and improve directly in this file.
"""

# Default files to use if no command line arguments
csv_file = '../data/test.csv' # Source file (CSV)
txt_file = '../data/test.txt' # File for VW (TXT)

from os.path import isfile
import sys
import csv
from datetime import datetime

'''
0 datetime - hourly date + timestamp  
1 season -  1 = spring, 2 = summer, 3 = fall, 4 = winter 
2 holiday - whether the day is considered a holiday
3 workingday - whether the day is neither a weekend nor holiday
4 weather - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
	2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
	3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
	4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog 
5 temp - temperature in Celsius
6 atemp - "feels like" temperature in Celsius
7 humidity - relative humidity
8 windspeed - wind speed
9 casual - number of non-registered user rentals initiated
10 registered - number of registered user rentals initiated
11 count - number of total rentals
'''

# Read command line
if len(sys.argv) >= 3:
	csv_file = sys.argv[1]
	txt_file = sys.argv[2]
if len(sys.argv) == 4:
	test = sys.argv[3] == 'test'

with open(csv_file,'r') as csvin, open(txt_file,'w') as txtout:
	cats = csvin.readline() # get categories
	cats = cats.split(',')
	
	if len(cats) == 12:
		test=False
	elif len(cats) == 9:
		test=True
	else:
		raise NameError('Check file format')
	
	csvin = csv.reader(csvin, delimiter=',')
	
	for row in csvin:
		
		# label
		if test:
			to_write = '0'
		else:
			to_write = row[11] # get the prediction

		to_write+=' |categorial'

		# datetime
		t = row[0].split(' ')
		
		# day
		d = t[0].split('-')
		d = datetime(int(d[0]),int(d[1]),int(d[2]))
		month = d.strftime("%B")
		to_write += ' ' + month
		day = d.strftime("%A")
		to_write += ' ' + day
		
		#hour
		t = t[1].split(':')
		to_write+=' h' + str(int(t[0]))

		# season, holiday, working day, weather (categorial)
		for i in range(1, 5):
			to_write+=' ' + cats[i][0:2] + row[i]
		
		# temp, atemp, humidity, windspeed (numeric)
		to_write+=' |numerical'
		for i in range(5, 9):
			to_write+=' ' + cats[i].strip('\n') + ':' + row[i]
		
		# casual, registered (numerical, not in test set)
		#if not(test):
		#	#to_write+=' |extra'
		#	for i in range(9, 11):
		#		to_write+=' ' + cats[i] + ':' + row[i]
		
		
		txtout.write(to_write + '\n')
