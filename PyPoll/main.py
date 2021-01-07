# Importing the OS module
import os

# Module for reading CSV file
import csv

# Setting path for CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

# Setting variables and initial values
votes = 0 # To count number of votes (/rows)
candidate_list = [] # List of candidates
unique_candidates = [] # Store unique candidates
votes_per_candidate = [] # How many votes did each candidate receive
percentage_of_votes = [] # Percentage of total vote

# Reading into CSV file
with open(csvpath) as csvfile:

    # Setting csvreader variable
    csvreader = csv.reader(csvfile)
    next(csvreader,None)
    # Defining data variable that can be referenced
    data = list(csvreader)
    # Looping through data
    for row in data:
        # Counting votes
        votes = votes + 1
        # Collect canidate names from third column
        candidate_list.append(row[2])
    # Create a set from above candidate_list for unique candidate names
    for x in set(candidate_list):
        unique_candidates.append(x)
        # Using variable y to hold number of votes per candidate
        y = candidate_list.count(x)
        votes_per_candidate.append(y)
        # Using variable z to hold percentage of total vote and rounding percentage
        z = round((y/votes)*100,3)
        percentage_of_votes.append(z)
    # Counting max percentage of votes
    winner_index = percentage_of_votes.index(max(percentage_of_votes))
    # Assigning the max percentage of votes to the correct candidate
    winner = unique_candidates[winner_index]

    # Printing all required outputs on separate lines and formatting votes to include thousand separators, couldn't figure out how to sort list of candidates in descending order based on percentage of votes
    print("Election Results" + "\n" + "----------------------------" + "\n" + "Total Votes: " + f'{votes:,}' + "\n" + "----------------------------")
    for candidate in range(len(unique_candidates)):
            print(unique_candidates[candidate] + ": " + str(percentage_of_votes[candidate]) + "% (" + f'{(votes_per_candidate[candidate]):,}' + ")")
    print("-------------------------" + "\n" + "Winner: " + winner + "\n" + "-------------------------")

    # Creating output file and exporting results to analysis folder
    output_file = 'analysis/results.txt'
    with open(output_file, "w") as txt_file:
        txt_file.write("Election Results")
        txt_file.write("\n----------------------------")
        txt_file.write("\nTotal Votes: " + f'{votes:,}')
        txt_file.write("\n----------------------------")
        for candidate in range(len(unique_candidates)):
            txt_file.write("\n" + unique_candidates[candidate] + ": " + str(percentage_of_votes[candidate]) + "% (" + f'{(votes_per_candidate[candidate]):,}' + ")")
        txt_file.write("\n----------------------------")
        txt_file.write("\nWinner: " + winner)
        txt_file.write("\n----------------------------")