# Needed Data
#1. Total number of votes cast
#2. Complete list of candidates who received votes
#3. Total number of votes each candidate received
# 4. Percentage of votes each candidate received
# 5. Winner of the election based on popular

import csv
import os

# Assign a vaiable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To Do: perform analysis
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)
  

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "W" mode we will write data to the file
with open(file_to_save, "w") as txt_file:
    # Write some data to the file
    txt_file.write("Counties in the Election\n-----------------\nArapahoe\nDenver\nJefferson")
  
