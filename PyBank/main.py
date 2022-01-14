# This PyBank program will read in a twp-column CSV file and then produce Financial Analysis that looks similar to below:
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)

import os
import csv

#Initialize variables
total_data_months=0  #Counts months of actual data (starts after header is read)
total_net=0
change_tally=0
average_change=0.0
greatest_increase=0
greatest_decrease=0
greatest_increase_month = "" 
greatest_decrease_month = "" 
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, encoding='utf-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader) # next consume a row
    #print ("csv_header= ",csv_header)
    last_row=0
    for row in csvreader:
        total_data_months += 1
        #print(f"{row}")
        total_net+=int(row[1])
        if total_data_months >1:  # Start calculating monthly change values beginning with 2nd row of data
            current_change=(int(row[1])-last_row)
            change_tally+=current_change
            if current_change >0 :  #Determine Greatest Increase
                if current_change>greatest_increase:
                    greatest_increase_month=row[0]
                    greatest_increase=current_change
            if current_change <0:   #Determine Greatest Decrease
                if current_change<greatest_decrease:
                    greatest_decrease_month=row[0]
                    greatest_decrease=current_change
        last_row=int(row[1])

    # Print final financial analysis on screen
    print("")
    print("Financial Analysis")
    print("-----------------------------")
    print("Total Months: "+str(total_data_months))
    print(f"Total: $"+str(total_net))
    average_change=(change_tally/(total_data_months-1)) 
    print("Average Change: $"+str(round(average_change,2)))
    print("Greatest Increase in Profits: " + str(greatest_increase_month) + " " + str(f"(${greatest_increase})"))
    print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " " + str(f"(${greatest_decrease})"))
    print("")

# save the output.txt file path
output_file = os.path.join('analysis', "output.txt")

# open the output.txt file and then write the finicial analysis to the txt file
with open(output_file, "w", encoding='utf-8', newline='') as datafile:
     writer = csv.writer(datafile)
     writer.writerow(["Financial Analysis"])
     writer.writerow(["-----------------------------"])
     writer.writerow(["Total Months: "+str(total_data_months)])
     writer.writerow([f"Total: $"+str(total_net)])
     writer.writerow(["Average Change: $"+str(round(average_change,2))])
     writer.writerow(["Greatest Increase in Profits: " + str(greatest_increase_month) + " " + str(f"(${greatest_increase})")])
     writer.writerow(["Greatest Decrease in Profits: " + str(greatest_decrease_month) + " " + str(f"(${greatest_decrease})")])
