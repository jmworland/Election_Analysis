# Election_Analysis

## Overview of Audit
We were approached by a client with the goal of writing code that would quickly go through large amounts of voting data and return easy to read vote counts broken down by county and candidate. The counts were then used to certify the winning candidate for the election. They also wanted this code to be easily adaptable to be used for other elections. 

## Election Audit results
The total amount of votes cast in this election was 369,711 with an overwhelming majority of those coming from Denver county. Denver county had 306,055 (82.8%), Jefferson county had 38,855 (10.5%), and Arapahoe county had 24,801 (6.7%). 

Candidate breakdown was similar with one candidate getting the overwhelming majority of votes. Diana DeGette was the winner with 272,892 votes (73.8%), Charles Casper Stockham with 85,213 votes (23.0%), and Raymon Anthony Doane with 11,606 votes (3.1%).

[Election Analysis](Analysis/election_analysis.txt)

## Election Audit Summary
We believe that we have written code that is ready made to be used for any election with minimal changes. As long as the data is provided in a CSV file then this code will work for any set of data. Most of the changes needed from election to election would be needed in two sections. The first section is in the variables that you would like to track. This will allow you to deal with data that provides more variables. Our current data basically only provided name of candidate and county, so if there is data provided that has more variables you would need to add them here.    

[Example 1](Resources/Code_Example_1.png)

The second section that would be most likely need to be changed is what results you would like to have displayed. 

[Example 2]
provide a business proposal to the election commission on how this script can be used with some modifications for any election, Give at least two examples of how the code can be modified to be used for other elections. 
