#Add our dependencies
import csv
import os
#The data we need to retrieve
file_to_load = os.path.join("Resources", "election_results.csv")
#Where it is going
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analyze the data
    file_reader = csv.reader(election_data)

    # Print header row.
    headers = next(file_reader)
    print(headers)

    


#1. Total number of votes cast.
#2. List all the candidates that received votes.
#3. Percentage of votes each candidate received. 
#4. Number of votes each candidate received.
#5. Winner of election based on popular vote. 
