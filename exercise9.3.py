#!/usr/bin/env python3

"""
Exercise  9.3: Write a program to read through a mail log, build a histogram
using a dictionary to count how many messages have come from each email
address, and print the dictionary.
Enter file name: mbox-short.txt
{'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3,
'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5,
'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1,
'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1,
'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}
Python for Everybody: Exploring Data Using Python 3
By Zackary Paulson
"""


thedict = dict()                   
fname = input('Enter file name: ')
try:
	fhand = open(fname)
except FileNotFoundError:
	print('File cannot be opened:', fname)
	exit()
	
for line in fhand:
	words = line.split()
	if len(words) < 2 or words[0] != 'From':
		continue
	else:
		if words[1] not in thedict:
			thedict[words[1]] = 1  	
		else:
			thedict[words[1]] += 1     			
print(thedict)