#1.Total number of votes cast
#2.A complete list of candidates who received votes
#3.Total number of votes each candidate received
#4.Percentage of votes each candidate won
#5.The winner of the election based on popular vote

import csv, os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
##file_to_load = 'Resources/election_results.csv'

## Open the election results and read the file.
##election_data = open(file_to_load, 'r')
## To do: perform analysis.
## Close the file.
##election_data.close()

with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

## Using the with statement open the file as a text file.
##outfile = open(file_to_save, "w")
## Write some data to the file.
##outfile.write("Hello World!")
## Close the file
##outfile.close()

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # Write three counties to the file.
     txt_file.write("Arapahoe\n")
     txt_file.write("Denver\n")
     txt_file.write("Jefferson")