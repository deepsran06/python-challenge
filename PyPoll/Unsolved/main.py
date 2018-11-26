# Import CSV and OS

import csv
import os

# Set Path for File

csvpath = os.path.join("..", "Resources", "election_data.csv")

# Define some of our Variables

candidates = []
votes = -1
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
    for name, num in vote_count.items():
        vote_percent[name] = str(round(((num/votes)*100),3)) + "% ("+str(num) + ")"

    # Use Vote Count to Find the Winner
    winner = max(vote_count.keys(), key=(lambda x: vote_count[x]))

    # Create Break Line and Format Print
    break_line = "-------------------------"
    print("Election Results")
    print(break_line)
    print(f"Total Votes: " + str(votes))
    print(break_line)
    for name, num in vote_percent.items():
        print(name, ":", num)
    print(break_line)
    print(f"Winner: " + str(winner))
    print(break_line)

# Set Variable for Output File
output_file = os.path.join("election_results.txt")

# Open Output File
writer = open(output_file, mode = "w")

# Print Results into Output File
writer.write("Election Results" + "\n")
writer.write(break_line + "\n")
writer.write(f"Total Votes: " + str(votes) + "\n")
for name, num in vote_percent.items():
    writer.write(name + ": " + num + "\n")
writer.write(break_line + "\n")
writer.write(f"Winner: " + str(winner) + "\n")
writer.write(break_line)
