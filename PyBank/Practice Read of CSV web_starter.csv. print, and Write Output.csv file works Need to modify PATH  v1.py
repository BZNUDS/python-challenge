import os
import csv

print("For homework can’t hardcode the CSV path (since Mac computers doesn’t have C: drive)")
csvpath = os.path.join('Resources', 'web_starter.csv')
#print(csvpath)
print("csvpath= "), csvpath

title = []
price = []
subscriber_count = []
num_reviews = []
course_length = []
print("csvpath=",csvpath)
with open(csvpath, encoding='utf-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    # csv_header = next(csvreader) # next consume a row

    for row in csvreader:
        print(f"{row[1]} this should happen about 1200 times")
        title.append(row[1]) # respective column in each row
        price.append(row[4])
        subscriber_count.append(row[5])
        num_reviews.append(row[6])
        course_length.append(row[7])
print("")
print("*****************************************")
print("For homework, can’t hardcode the CSV path (since Mac computers doesn’t have C: drive)")
print("")
courses = zip(title, price, subscriber_count, num_reviews, course_length)

# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", encoding='utf-8', newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Title", "Price", "Subscriber Count", "Number of Reviews", "Course Length"])

    writer.writerows(courses)