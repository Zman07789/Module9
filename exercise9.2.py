#Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with “From”, then look for the third word and keep a running count of 
# each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

#Sample Line:

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Sample Execution:
#Enter a file name: mbox-short.txt
#{'Fri': 20, 'Thu': 6, 'Sat': 1}
# By Zackary Paulson


fname = input('Enter a file name: ')
fhand = open(fname)
dates = dict()

try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()
    
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dates:
            dates[words[2]] = 1      
        else:
            dates[words[2]] += 1      
            
print(dates)
        
        
        


    