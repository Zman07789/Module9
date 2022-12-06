#Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

#Enter file name: mbox-short.txt
#{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
#	'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
#	'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
#	'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
#	'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
#	'ray@media.berkeley.edu': 1}
# By Zackary Paulson


nbane = input("Enter file:")
if len(nbane) < 1:
	nbane = "mbox-short.txt"
handle = open(nbane)

lst = list()

for line in handle:
	if not line.startswith("From:"): continue
	line = line.split()
	lst.append(line[1])
	
counts = dict()
for word in lst:
	counts[word] = counts.get(word,0) + 1
	
bigcount = None
bigword = None
for word,count in counts.items(): 
	if bigcount is None or count > bigcount:
		bigcount = count
		bigword = word
		
print (bigword,bigcount)