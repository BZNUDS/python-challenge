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

#Initialize variables
total_votes=0  #Counts up number of actual votes (starts after header is read)
total_candidates=0
candidates=[]
winner=""

print("")
print("Need to change hardcoded csvpath from mini_election_data.csv to election_data.csv")

#csvpath = os.path.join('Resources', 'election_data.csv')
csvpath = os.path.join('Resources', 'mini_election_data.csv')

with open(csvpath, encoding='utf-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader) # next consume a row
    print ("csv_header= ",csv_header)
    last_row=0
    for row in csvreader:
        total_votes += 1
        print(f"{row}")
        print(f"{total_votes}")
        

        # if total_data_months >1:  # Start calculating monthly change values beginning with 2nd row of data
        #     current_change=(int(row[1])-last_row)
        #     change_tally+=current_change
        #     if current_change >0 :  #Determine Greatest Increase
        #         if current_change>greatest_increase:
        #             greatest_increase_month=row[0]
        #             greatest_increase=current_change
        #     if current_change <0:   #Determine Greatest Decrease
        #         if current_change<greatest_decrease:
        #             greatest_decrease_month=row[0]
        #             greatest_decrease=current_change
        # last_row=int(row[1])

    # Print final financial analysis on screen
    # print("")
    # print("Financial Analysis")
    # print("-----------------------------")
    # print("Total Months: "+str(total_data_months))
    # print(f"Total: $"+str(total_net))
    # average_change=(change_tally/(total_data_months-1)) 
    # print("Average Change: $"+str(round(average_change,2)))
    # print("Greatest Increase in Profits: " + str(greatest_increase_month) + " " + str(f"(${greatest_increase})"))
    # print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " " + str(f"(${greatest_decrease})"))
    # print("")

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
