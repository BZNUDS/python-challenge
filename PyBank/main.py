# This PyBank program will read in a twp-column CSV file and then produce Financial Analysis that looks similar to below:
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)

import os
import csv
total_months=0
total_net=0
average=0
greatest_increase=0
greatest_decrease=0

csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)

title = []
price = []
subscriber_count = []
num_reviews = []
course_length = []
print("csvpath=",csvpath)
with open(csvpath, encoding='utf-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    #csv_header = next(csvreader) # next consume a row
    #print ("csv_header= "),csv_header

    for row in csvreader:
        print(f"{row}")
        #print(f"{row[1]}")
        #total_net+=int(row[1])
        #print("total_net="), total_net
        # title.append(row[1]) # respective column in each row
        # price.append(row[4])
        # subscriber_count.append(row[5])
        # num_reviews.append(row[6])
        # course_length.append(row[7])

# courses = zip(title, price, subscriber_count, num_reviews, course_length)

# # save the output file path
# output_file = os.path.join('analysis', "output.csv")

# # open the output file, create a header row, and then write the zipped object to the csv
# with open(output_file, "w", encoding='utf-8', newline='') as datafile:
#     writer = csv.writer(datafile)

#     writer.writerow(["Title", "Price", "Subscriber Count", "Number of Reviews", "Course Length"])

#     writer.writerows(courses)