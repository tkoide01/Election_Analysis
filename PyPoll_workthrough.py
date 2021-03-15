# The data we need to retrieve.
# 1．The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The perventage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is", now)

# Import the csv module
import csv
dir(csv)

dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})

dir(str)
dir(int)
dir(float)
dir(bool)
dir(list)
dir(tuple)
dir(dict)

import random
import numpy

# Assign a variable for the file to load and the path.
file_to_load ='Resources/election_results.csv'
# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()

# Open the election results and read the file
file_to_load = 'Resources/election_results.csv'
with open(file_to_load) as election_data:

    # To do: perform analysis.
    print(election_data)

import os
dir(os)
dir(os.path)

# Complete set of steps to load data
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
    print(election_data)

# Create a filename variable to a direct or indirect paht to the file.
import csv
import os
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")
# Close the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
    # or
    txt_file.write("Counties in the Election\n------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")


# Add our dependencies.
import csv
import os
# Assign a variabe to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to ssave the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Print each row in the CSV files.
    for row in file_reader:
        print(row[0])
    for row in file_reader:
        print(row)
# Open the election results and rad the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)  

# Get the Total Votes
# Add our dependencies.
import csv
import os
# Assign a variabe to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to ssave the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
   
    # Read each row in the CSV files.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes.
print(total_votes)

# Get the Candidates in the election

# As the Candidate column is the third column that has the second index, 
# we use row[2] to refer the Candidate column.

# Add our dependencies.
import csv
import os
# Assign a variabe to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to ssave the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
   
    # Read each row in the CSV files.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Check if the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)

# Get the Candidates' Votes
# now, count the votes for each canddate in the 'if' statement
# we do this by creating a dictioary with the key as candidate name and their vote is the value for the key

# Add our dependencies.
import csv
import os
# Assign a variabe to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to ssave the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
# Declare the empty dictionary
candidate_votes ={}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
   
    # Read each row in the CSV files.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Check if the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        # note that indent is different from the previous code to avoid resetting value equal 0 after incrementing
        candidate_votes[candidate_name] += 1

# Print the candidate vote dictionary.
print(candidate_votes)


# Determine Candidates' Percentage of Votes

vote_percentage = ( votes / total_votes ) *100
# votes are the values of each candidate_name in the candidate_votes
# we need to convert votes and total_votes to floating-point decimal numbers beause they are integers

# Follow below steps to retrieve the votes for each cnadidate and get the percentage of voets:
# 1. Use a for loop to iterate through the candidate_options = [] list. We will get the candidates' name
# 2. Use the for loop variable to retrieve the votes of the candidate from the candidate_votes = {} dictionary
# 3. Calc the percentage of the vote count
# 4. Print each candidate and the percentage of votes using f-string formatting

# Initialize a total vote counter
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
# Declare the empty dictionary
candidate_votes ={}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
   
    # Read each row in the CSV files.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Check if the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        # note that indent is different from the previous code to avoid resetting value equal 0 after incrementing
        candidate_votes[candidate_name] += 1

# Determine the percetage of votes for each candidate by looping through the counts.
# Indent the followings codes back to as it is not a part of for loop nor if statement
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Prin the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")


# Determine the Winning Candidate
# Now, use the decision statement to compare the number of votes each candidate received.

# When we loop through the vote counts, we can:
    # Use an if statement to cehck if teh first vote count for a candidate is greaer than zero.
    # If the statement is tru, then that vote count will be equal to the "winning count."
    # At the same time, we can set that candidate's percentage of the vote equal to the "winning percentage."
    # Then we can sleect the candiadate as the "winning candidate" from the candidate_option list.
# To do the above, we will first neead to:
    # Declare a variable that holds a empty string value for the winning candidate.
    # Declare a variable for the "winning_count" equal to zero.
    # Declare a variable for the "winning_percentage" equal to zero.
# Next, willcreate an if statement inside the for loop and do:
    # Determine if the vote count that was calculated is greater than the winning_count.
    # If he vote count is greater than the winning_count and the percentage is greater than the winning_percentage, 
    # set the winning_count equal to votes and set the winning_percentage equal to teh vote_percentage.
    # Set the winning_count equal to the cairable, candidate_name, in the for loop.
    #  

# Add our dependencies.
import csv
import os
# Assign a variabe to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to ssave the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0
# Candidate Options
candidate_options = []
# Declare the empty dictionary
candidate_votes ={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Read each row in the CSV files.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Check if the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        # note that indent is different from the previous code to avoid resetting value equal 0 after incrementing
        candidate_votes[candidate_name] += 1

# Determine the percetage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Prin the candidate name and percentage of votes.

    # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

    # Determin winning cote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percentage = vote_percentage;
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

# To do: print out the winning candidate, vote count and percentage to terminal
Winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Cout: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"-------------------------\n")
print(Winning_candidate_summary)