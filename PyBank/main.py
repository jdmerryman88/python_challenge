import os
import csv

pybank_csv = '/Users/justinmerryman/Documents/Rice-BootCamp-Homeworks/python_challenge/PyBank/Resources/budget_data.csv'

months = 0
greatest_increase = 0
greatest_decrease = 0
average_change = 0
greatest_month = "Jan-2020"
worst_month = "Jan-2020"

# Open and read csv
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(csv_header)

    for row in csv_reader:
        months = months + 1
        change = float(row[1])
        average_change = average_change + change
        if greatest_increase > change:
            greatest_increase = change
            greatest_month = row[0]
        
    print(months)
    print(average_change / months)





