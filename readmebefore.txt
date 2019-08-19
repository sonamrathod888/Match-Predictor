To run PHASE 1

IN phase 1 directory,first execute the webscraping script and then,
In terminal type 
$ pyspark
next open KMCBat.ipynb and execute it , after this batsmen cluster will be formed and the output will be stored in the batcluster.csv
next open KMCBowl.ipynb and execute it , after this batsmen cluster will be formed and the output will be stored in the bowlcluster.csv


To run PHASE 2

first calculate the probabilities in step1 and step2 directories by simply executing the files there,this will be used as input next
next in simulation directory open pyspark and run big_data_final.ipynb which will give the cluster probabilities
next to simulate a match just run the simulation.ipynb ,it will print out the result


To run PHASE 3

open pyspark
next run decision_tree.ipynb,this will create two decision tree one for "runs" and the other for "wicket",which will be used in the prediction of the outcome of each over while simulating

