#1.Total number of votes cast
#2.A complete list of candidates who received votes
#3.Total number of votes each candidate received
#4.Percentage of votes each candidate won
#5.The winner of the election based on popular vote

import csv, os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter, candidate options and votes
total_votes = 0
candidate_options = list()
candidate_votes = dict()

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


with open(file_to_load) as election_data:
     
     # To do: perform analysis.

     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)

#    # Read the header row.
     headers = next(file_reader)

    # Print each row in the CSV file.
     for row in file_reader:
        # Adding to the total vote count.
        total_votes += 1
        # Adding candidate name
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
     election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
     print(election_results, end="")
    # Save the final vote count to the text file.
     txt_file.write(election_results)     

     # Determine the percentage of votes for each candidate by looping through the counts.
     # Iterate through the candidate list.
     for candidate in candidate_votes:
          # Retrieve vote count of a candidate.
          votes = candidate_votes[candidate]
          # Calculate the percentage of votes.
          vote_percentage = votes / total_votes * 100

          # Print out each candidate's name, vote count, and percentage of
          # votes to the terminal.
          candidate_results=(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
          # Print each candidate, their voter count, and percentage to the terminal.
          print(candidate_results)
          #  Save the candidate results to our text file.
          txt_file.write(candidate_results)

          #Determine winning vote count and candidate
          # Determine if the votes is greater than the winning count.
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # If true then set winning_count = votes and winning_percent =
               # vote_percentage.
               winning_count = votes
               winning_percentage = vote_percentage
               # And, set the winning_candidate equal to the candidate's name.
               winning_candidate = candidate

     #Winning summary        
     winning_candidate_summary = (
     f"-------------------------\n"
     f"Winner: {winning_candidate}\n"
     f"Winning Vote Count: {winning_count:,}\n"
     f"Winning Percentage: {winning_percentage:.1f}%\n"
     f"-------------------------\n")
     print(winning_candidate_summary, end="")
     #writing winning summary in .txt file
     txt_file.write(winning_candidate_summary)