# # This PyPoll program will read poll data from a three-column CSV file called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# My task is to create a Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.

    # As an example, your analysis should look similar to the one below:
        # Election Results
        # -------------------------
        # Total Votes: 3521001
        # -------------------------
        # Khan: 63.000% (2218231)
        # Correy: 20.000% (704200)
        # Li: 14.000% (492940)
        # O'Tooley: 3.000% (105630)
        # -------------------------
        # Winner: Khan
        # -------------------------

# In addition, your final script should both print the analysis to the terminal and export a text file with the results. Analysis that looks similar to below:

import os
import csv
from re import I

#Initialize variables
total_votes=0  #Counts up number of actual votes (starts after header is read)
candidates_lists=[]
candidates_short_lists=[]
candidates_count_lists=[]
candidates_percent_lists=[]
total_candidates=0
current_index=0
current_count=0
i=0
j=0
max_votes=0
max_votes_index=0
winner=""

#csvpath = os.path.join('Resources', 'mini_election_data.csv')  #Brian's test file
#print("need to chage, using mini_election_data.csv for testing puposes")
csvpath = os.path.join('Resources', 'election_data.csv')
#print("")

with open(csvpath, encoding='utf-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader) # next consume a row
    #print ("csv_header= ",csv_header)

    for row in csvreader:
        total_votes += 1
        #print(f"{row}")
        candidates_lists.append(row[2])
        if row[2] not in candidates_short_lists:
            candidates_short_lists.append(row[2])

#print("candidates_short_lists",candidates_short_lists)

for i in range(0,len(candidates_short_lists)):
    current_count=0
    for j in range(0,len(candidates_lists)):
        if candidates_short_lists[i] == candidates_lists[j]:
            current_count += 1
         
    candidates_count_lists.append(current_count)
    #print("candidates_count_lists=",candidates_count_lists)

find_max_votes = 0
for i in range(0,len(candidates_short_lists)):
    candidates_percent_lists.append((candidates_count_lists[i] / total_votes)*100.0)
    #print("candidates_percent_lists[i]=", (round(candidates_percent_lists[i],5)))
    if candidates_count_lists[i] > max_votes:
        max_votes = candidates_count_lists[i]
        max_votes_index = i

# Print out resluts formated per the instructions
# print(f"Election Results")
# print("-------------------------")
# print(f"Total Votes: ",total_votes)
# print(f"-------------------------")
# for i in range(0,len(candidates_short_lists)):
#     print(f"{candidates_short_lists[i]}:", f"{candidates_percent_lists[i]:.3f}%",f"({candidates_count_lists[i]})")
# print(f"-------------------------")
# print(f"Winner: ",candidates_short_lists[max_votes_index])
# print(f"-------------------------")
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")

for i in range(0,len(candidates_short_lists)):
    output=output+(f"{candidates_short_lists[i]}: {candidates_percent_lists[i]:.3f}% ({candidates_count_lists[i]})\n")
    #print(f"{candidates_short_lists[i]}: {candidates_percent_lists[i]:.3f}% ({candidates_count_lists[i]})")
output=output+(f"-------------------------\n")
output=output+(f"Winner: {candidates_short_lists[max_votes_index]}\n")
output=output+(f"-------------------------\n")
    
print(output)
# save the output.txt file path
output_file = os.path.join('analysis', "output.txt")

# open the output.txt file and then write the finicial analysis to the txt file
# with open(output_file, "w", encoding='utf-8', newline='') as datafile:
#      writer = csv.writer(datafile)
#      writer.writerow(["Financial Analysis"])
#      writer.writerow(["-----------------------------"])
#      writer.writerow(["Total Months: "+str(total_data_months)])
#      writer.writerow([f"Total: $"+str(total_net)])
#      writer.writerow(["Average Change: $"+str(round(average_change,2))])
#      writer.writerow(["Greatest Increase in Profits: " + str(greatest_increase_month) + " " + str(f"(${greatest_increase})")])
#      writer.writerow(["Greatest Decrease in Profits: " + str(greatest_decrease_month) + " " + str(f"(${greatest_decrease})")])
# print(f"Election Results")
# print("-------------------------")
# print(f"Total Votes: ",total_votes)
# print(f"-------------------------")
# for i in range(0,len(candidates_short_lists)):
#     print(f"{candidates_short_lists[i]}:", f"{candidates_percent_lists[i]:.3f}%",f"({candidates_count_lists[i]})")
# print(f"-------------------------")
# print(f"Winner: ",candidates_short_lists[max_votes_index])
# print(f"-------------------------")
