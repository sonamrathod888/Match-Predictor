import time
import csv
import operator
from collections import Counter
l=[]
with open('finalcsv.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file)
	for line in csv_reader:
		try:
			l.append([line[4],line[6],line[7]])
			#print [line[4],line[6],line[7]]
		except IndexError: 
			pass
ba=[]
ba=l		
#l.sort(key = operator.itemgetter(0, 1))

"""
print(len(l))
time.sleep(1)
A=[]
for line in l:
	A.append([line[0],line[1]])
	
print A
ll=[]
#this has the total number of batsmen bowler count
for x in set(map(tuple, A)):
    	#print '{} = {}'.format(x, A.count(list(x)))
	ll.append([x[0],x[1],A.count(list(x))])
    #i=i+1	
    #print(i)
for line in ll:
	print line
print ll

"""

#this has the total number of batsem bowler and runs count
i=0
ba.sort(key = operator.itemgetter(0, 1,2))
bfin=[]
for x in set(map(tuple, ba)):
    	print '{} = {}'.format(x, ba.count(list(x)))
	bfin.append([x[0],x[1],x[2],ba.count(list(x))])
	#bfin[x]=ba.count(list(x))	
print bfin




