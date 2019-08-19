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
l.sort(key = operator.itemgetter(0, 1))

print(len(l))
time.sleep(1)
A=[]
for line in l:
	A.append([line[0],line[1]])
	
print A
ll=[]
for x in set(map(tuple, A)):
    	#print '{} = {}'.format(x, A.count(list(x)))
	ll.append([x[0],x[1],A.count(list(x))])
    #i=i+1	
    #print(i)
for line in ll:
	print line
#print ll
with open('finaltotalcount.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for line in ll:
	wr.writerow(line)
print "writing1 done"
#this has the total number of batsem bowler and runs count
i=0
ba.sort(key = operator.itemgetter(0, 1,2))
bfin=[]




i=0
for x in set(map(tuple, ba)):
    	print '{} = {}'.format(x, ba.count(list(x)))
	bfin.append([x[0],x[1],x[2],ba.count(list(x))])
	#bfin[x]=ba.count(list(x))	
	i=i+1
	print i
#print bfin

with open('finalbatruncount.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for line in bfin:
	wr.writerow(line)

"""
one=0
two=0
three=0
four=0
six=0
final=[]
for line in ll:
	for line2 in bfin:
		if(line[0]==line2[0]and line[1]==line2[1]):
			if(line2[2]==0):
				one=line2[3]/line[2]
				print one
			if(line2[2]==0):
				two=line2[3]/line[2]
				print two
			if(line2[2]==0):
				three=line2[3]/line[2]
				print three
			if(line2[2]==0):
				four=line2[3]/line[2]
				print four
			if(line2[2]==0):
				six=line2[3]/line[2]
				print six
			time.sleep(1)





for i in range(len(l)):
	j=i
	c=0
	for j in range(len(l)-1):
		if(l[i][1]==l[j][1] and l[i][0]==l[j][0]):
			print(l[i][0],l[i][1])
			c=c+1
		else:
			i=i+c
		print(c)
	print(i)
	time.sleep(1)
"""
