import os
import csv

#pybank_csv = os.path.join('Resources/budget_data.csv')

pybank_csv = '/Users/justinmerryman/Documents/Rice-BootCamp-Homeworks/python_challenge/PyBank/Resources/budget_data.csv'
#

months = 0
greatest_increase = int(0)
greatest_decrease = int(0)
average_change = []
greatest_month = "Jan-2020"
worst_month = "Jan-2020"
total_change = float(0) 
total = 0

# Open and read csv
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(csv_header)

    for row in csv_reader:
        months = months + 1
        change = int(row[1])
        total = total + change
        average_change.append(row[1])
        


        if change >= greatest_increase:
            greatest_increase = change
            greatest_month = row[0]

        elif change <= greatest_decrease:
            greatest_decrease = change
            worst_month = row[0]
        
initial = float(average_change[0])
difference = 0
for x in range(len(average_change)):
    if x  == 0:
        difference = 0
    else:
        difference = float(average_change[x]) - initial
        total_change = total_change + difference
        initial = float(average_change[x])
        print(difference)


total_months_output = "Total Months: " + str(months)
output_avg = total_change / (months - 1) 
output_avg = ("%.2f" % output_avg)
print(total_change)
#output_path = os.path.join('analysis/analysis.txt')

output_path = '/Users/justinmerryman/Documents/Rice-BootCamp-Homeworks/python_challenge/PyBank/analysis/analysis.txt'

# Open the file using "write" mode. Specify the variable to hold the contents
file = open(output_path, 'w',)
file.write("Financial Analysis \n")
file.write("------------------------------------- \n")
file.write(total_months_output)
file.write("\n")
file.write("Total: $" + str(total))
file.write("\n")
file.write("Average_Change: $" + str(output_avg))
file.write("\n")
file.write("Greatest Increase in Profits: " + greatest_month + " ($" + str(greatest_increase) + ")")
file.write("\n")
file.write("Greatest Decrease in Profits: "+ worst_month + " ($" + str(greatest_decrease) + ")")
file.write("\n")
file.write("")
file.close()

    
    
print("Financial Analysis")
print("--------------------------------------")
print("Total Months: " + str(months) )
print("Total: $" + str(total))
print("Average_Change: $" + str(output_avg))
    
print("Greatest Increase in Profits: " + greatest_month + " ($" + str(greatest_increase) + ")")

print("Greatest Decrease in Profits: "+ worst_month + " ($" + str(greatest_decrease) + ")")
print(" ")
    






