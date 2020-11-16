import os
import csv

pypoll_csv = '/Users/justinmerryman/Documents/Rice-BootCamp-Homeworks/python_challenge/PyPoll/Resources/election_data.csv'

vote = 0
candidates = {"name": "Blank", "votes": 0}
candidate = "John Doe"
greatest_increase = int(0)
greatest_decrease = int(0)
average_change = int(0)
greatest_month = "Jan-2020"
worst_month = "Jan-2020"

# Open and read csv
with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(csv_header)

    for row in csv_reader:
        vote = vote + 1
        print(row[2])
        
        
        


        #if change >= greatest_increase:
         #   greatest_increase = change
          #  greatest_month = row[0]

        #elif change <= greatest_decrease:
         #   greatest_decrease = change
          #  worst_month = row[0]

total_vote_output = "Total Votes: " + str(vote)
output_path = '/Users/justinmerryman/Documents/Rice-BootCamp-Homeworks/python_challenge/PyPoll/analysis/analysis.txt'

# Open the file using "write" mode. Specify the variable to hold the contents
file = open(output_path, 'w',)
file.write("Election Results \n")
file.write("------------------------------------- \n")
file.write(total_vote_output)
file.write("\n")
file.write("------------------------------------- \n")
#file.write("Total: $" + str(average_change))
#file.write("\n")
#file.write("Average_Change: $" + str(average_change / months))
#file.write("\n")
#file.write("Greatest Increase in Profits: " + greatest_month + " ($" + str(greatest_increase) + ")")
#file.write("\n")
#file.write("Greatest Decrease in Profits: "+ worst_month + " ($" + str(greatest_decrease) + ")")
#file.write("\n")
#file.write("")
#file.close()

    
    
print("Financial Analysis")
print("--------------------------------------")
print("Total Votes: " + str(vote))
print("--------------------------------------")
#print("Total: $" + str(average_change))
#print("Average_Change: $" + str(average_change / months))
    
#print("Greatest Increase in Profits: " + greatest_month + " ($" + str(greatest_increase) + ")")

#print("Greatest Decrease in Profits: "+ worst_month + " ($" + str(greatest_decrease) + ")")
#print(" ")
    

print candidates["name"][0]











