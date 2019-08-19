import csv
import time
bfin=[]
ll=[]
with open('finalbatruncount.csv','r') as csv_file:
	r = csv.reader(csv_file)
	for line in r:
		bfin.append(line)
	

with open('finaltotalcount.csv','r') as csv_file:
	r = csv.reader(csv_file)
	for line in r:
		ll.append(line)
#print bfin
#print ll
				





one=0
two=0
three=0
four=0
six=0
final=[]
for line in bfin:
	for line2 in ll:
		if(line[0]==line2[0]and line[1]==line2[1]):
			print((line[2]))

			if(int(line2[2])==0):
				zero=int(line2[3])/int(line[2])
				print one
			if(int(line2[2])==1):
				one=int(line2[3])/int(line[2])
				print one
			if(int(line2[2])==2):
				two=int(line2[3])/int(line[2])
				print two
			if(int(line2[2])==3):
				three=int(line2[3])/int(line[2])
				print three
			if(int(line2[2])==4):
				four=int(line2[3])/int(line[2])
				print four
			if(int(line2[2])==6):
				six=int(line2[3])/int(line[2])
				print six
			time.sleep(1)


