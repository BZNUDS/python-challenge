import os
import csv
i=0

print("Start of Program v0.4 before udemy print") 
#csvpath = os.path.join('Resources', 'web_starter.csv')
udemy_csv = os.path.join('Resources', 'web_starter.csv')
#udemy_csv = os.path.join('..', 'BZ Northwestern BC', 'Class', 'python-challenge', 'PyBank', 'Resources', 'web_starter.csv') 
#udemy_csv = "Users\BZ Northwestern BC\Class\python-challenge\PyBank\Resources\web_starter.csv"
print("udemy_csv=",udemy_csv)
print("Start of Program v0.4 after udemy print") 
# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

# Use encoding for Windows
# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
print("udemy_csv before open=",udemy_csv)
with open(udemy_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        print("row=",row)
        # while i <= 100:
        #     if i ==99:
        #         print("i=99")
        #         print("row=",row) 
        #     i += 1
        # Add title
        title.append(row[1])

        # Add price
        price.append(row[4])

        # Add number of subscribers
        subscribers.append(row[5])

        # Add amount of reviews
        reviews.append(row[6])

        # Determine percent of review left to 2 decimal places
        percent = round(int(row[6]) / int(row[5]), 2)
        review_percent.append(percent)

        # Get length of the course to just a number
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))

# # Zip lists together
# cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

# # Set variable for output file
# output_file = os.path.join("web_final.csv")

# #  Open the output file
# with open(output_file, "w", newline="") as datafile:
#     writer = csv.writer(datafile)

#     # Write the header row
#     writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
#                      "Percent of Reviews", "Length of Course"])

#     # Write in zipped rows
#     writer.writerows(cleaned_csv)
