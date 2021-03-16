#Add our dependencies
import csv
import os
#The data we need to retrieve
file_to_load = os.path.join("Resources", "election_results.csv")
#Where it is going
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Set vote count to 0
total_votes = 0

#Candidate Choices
candidate_options = []
candidate_votes = {}

#Winning candidate stuff
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analyze the data
    file_reader = csv.reader(election_data)

    #Read header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        #Tally votes
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #Check candidate has not been added already
        if candidate_name not in candidate_options:
            
            #Add candidates to the list
            candidate_options.append(candidate_name)

            #Track individual votes
            candidate_votes[candidate_name] = 0
        
        #Tally individual votes
        candidate_votes[candidate_name] += 1

#Determine the percentage of votes per candidate
#1 Go through the list
for candidate_name in candidate_votes:
    #2 Get number of votes per candidate
    votes = candidate_votes[candidate_name]
    #3 Calculate percentage
    vote_percentage = float(votes) / float(total_votes) * 100
    
    #4 Print name and percentage
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count.
    if(votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percent = 
        #vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #Set winning_candidate to candidate name.
        winning_candidate = candidate_name
    
#Print out winning candidate and counts
winning_candidate_summary = (f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------")
print(winning_candidate_summary)

