# Match-Predictor

Introduction
The Project is mainly about predicting the results of ipl matches, using the old ipl match histroy. Here we are analysing the old match results, based on that we are judging the outcome of randomly chosen match and varifying the accuracy of prediction with actual result. Approach: 1)Normal approach using clustering Here we are creating batsman and bowler clusters using K means algorithm. 2)Decision Tree approach Here we are Converting the data into decision tree model and using this we are predicting the result

Phase 1

Reference to get ipl data 1)www.espncricinfo.com/ Using this website we scrape the html to get the player list with differnt attributes like runs, balls faced, strike rate, avarage, etc..

Initially we scrape each individual team data later using this data we merged all and extracted the dataset which we wanted.

Links for each individual team data :
http://stats.espncricinfo.com/ci/engine/records/averages/batting.html?id=117;team=4343;type=trophy similarly Change team id with 4347, 4344, 5845, 4342, 4788, 4341, 4346, 4787, 4345, 5843 to get individual tam data We have used BeautifulSoup python libary to scrape the html and extract data

We loaded the dataset to HDFS to make clusters.
we are checking the batsman and bowler combination in the original dataset to use it for prediction, but there are some batsman and bowler combination did not occur in the dataset, in order to overcome this we used concept of clusering. Clustering is mainly putting every batsman and bowler in a perticular cluster number between 1 to 10 using K means algorithm. And based on the parametre we are judging which specific cluster the player belongs to, the parametres are strike rate, avarage, runs scored and ball faced for batsman and for bowler we are taking wickets taken, overs bowled, bowling avarage, bowling strike rate and economy.
For the new players we are assinging the values of cluster for which he belongs to.

The parameters used for clustering batsman – Runs, Strike Rate, Average, balls faced
The parameters used for clustering bowlers – Wickets, Economy, Average, Strike Rate, overs bowled,

Phase 2


Input: sequence of batsman order for both innings stored in seperate list. Similarly for every over for both innings we created list with bowler we are using score1, score2 and wickets variable to add runs and wickets using the clusters of batsman and bowler we created cluster vs cluster statistics using original dataset for ball by ball result of all matches till 2018. In cluster vs cluster data we assigned probabilities for each kind of run using batsman and bowler cluster Every time a new combination was encountered, we found the batsman cluster number and the bowler cluster number and added the parameters to the corresponding cluster combination. Finally probabilities of scoring 0s,1s,2s,3s,4s,6s,not_out were obtained for every cluster combination by dividing by the total number of balls.
And we also created a file which contain batsam and bowler combination with cluster number of both and probabilities of scoring 0,1,2,3,4,6,out We wrote a python code to simulate an entire IPL match using ball by ball prediction. To predict the outcome of a ball, we searched for the batsman-bowler combination in the statistics file. For any new occurence we took the value from specific cluster for which a batsman and bowler belongs, inorder to simulate. A list of cumulative probabilities is constructed from the probabilities obtained.For new players we generated a random number between 1 to 10 and assigned to a player and given his cluster number as that random number to simulate the result. The outcome could be 0,1,2,3,4,6 or a wicket. This is repeated for all balls until 20 overs are up or there are no wickets left. Using score variables checking which team has won and fiding the accuracy for prediction.

Phase 3


Here then we followed the method of using the decision trees. The outcome of the match was predicted using the decision trees.
Using the phase 2 statistics we use the data and we perform to predict the score again ball by ball. Using the Spark MLLIB which provides functions to train and construct Decision Tree models. We trained a decision tree model, with the following parameters: Batting Average, Batting Strike Rate, Bowling Average, Bowling Economy, Bowling Strike Rate, No of balls (represented with the overs), Innings and finally the Runs. This is trained into the regression tree and thus is later used to predict the possible outcomes for the particular match. Thus we simulate the match give and predict on the basis of the trained decision tree.

EXPERIMENTAL RESULTS
For clustering –
Accuracy : 75.21%
Error : 24.79%

For Regression decision trees –
Accuracy : 82.89%
Error : 17.11%
