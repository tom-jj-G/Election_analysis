import csv, os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter, candidate options, votes and counties objects
total_votes = 0
candidate_options = list()
candidate_votes = dict()
county_options = list()
county_votes = dict()
county_vote = 0

# County with the biggest turnout and its Count Tracker
biggest_county = ""
biggest_count = 0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


with open(file_to_load) as election_data:
     
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)

     # Read the header row.
     headers = next(file_reader)

    # Print each row in the CSV file.
     for row in file_reader:

          # Part 1/2: Votes analysis for candidates
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


          # Part 2/2: Votes analysis for counties
          # Adding county name
          county_name = row[1]

          # If the county does not match any existing county...
          if county_name not in county_options:
               # Add it to the list of counties.
               county_options.append(county_name)
               #Begin tracking that county's vote count. 
               county_votes[county_name] = 0

          # Add a vote to that county's count
          county_votes[county_name] += 1


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


     # Part 1/2: Print counties' results 
     # Display and save county titles
     county_titles = (
          f"\nCounty Votes:\n")
     print(county_titles, end="")
     txt_file.write(county_titles)
     
     # Determine the percentage of votes for each county by looping through the counts.
     # Iterate through the county list.
     for county in county_votes:
          # Retrieve vote count of a county.
          votes = county_votes[county]
          # Calculate the percentage of votes.
          vote_percentage = votes / total_votes * 100

          # Print out each county's name, vote count, and percentage of
          # votes to the terminal.
          county_results=(f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
          # Print each county, its voter count, and percentage to the terminal.
          print(county_results)
          # Save the county results to our text file.
          txt_file.write(county_results)

          # Determine the county with the biggest turnout
          # Determine if the votes is greater than the biggest count.
          if (votes > biggest_count):
               # If true then set biggest_count = votes
               biggest_count = votes
               # And, set the biggest_county equal to the county's name.
               biggest_county = county

     #Biggest county summary        
     biggest_county_summary = (
     f"\n-------------------------\n"
     f"Largest County Turnout: {biggest_county}\n"
     f"-------------------------\n")
     print(biggest_county_summary, end="")
     #writing biggest county summary in .txt file
     txt_file.write(biggest_county_summary)


     # Part 2/2: Print candidates' results 
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