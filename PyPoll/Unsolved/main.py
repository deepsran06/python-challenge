# Import CSV and OS

import csv
import os

# Set Path for File

csvpath = os.path.join("..", "Resources", "election_data.csv")

# Define What We Are Looking For

candidates = []
votes = 0
vote_count = {}
vote_percent = {}

# Read the CSV File
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Going to count the number of votes and the list of candidates
    for row in csvreader:

        # Track the votes
        votes = votes + 1

        # Track list of candidates with votes
        if row[2] not in candidates and row[2] not in "Candidate":
            candidates.append(row[2])
            vote_count[row[2]] = 1
        elif row[2] in candidates and row[2] not in "Candidate":
            vote_count[row[2]] = vote_count[row[2]] + 1

# Calculations for Percentage of Vote
    for key, value in vote_count.items():
        vote_percent[key] = str(round(((value/votes)*100),3)) + "% ("+str(value) + ")"

    # Use Vote Count to Find the Winner
    winner = max(vote_count.keys(), key=(lambda k: vote_count[k]))

    # Create Break Line and Format Print
    break_line = "-------------------------"
    print("Election Results")
    print(break_line)
    print(f"Total Votes: " + str(votes))
    print(break_line)
    for key, val in vote_percent.items():
        print(key, ":", val)
    print(break_line)
    print(f"Winner: " + str(winner))
    print(break_line)

