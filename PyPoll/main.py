import os
import csv


pypoll_csv = os.path.join('Resources/election_data.csv')
#pypoll_csv = '/Users/justinmerryman/Documents/Rice-BootCamp-Homeworks/python_challenge/PyPoll/Resources/election_data.csv'

total_vote = 0
candidates = {}
vote_count = []
votes = []
z = []
names = []
totals = []
percents = []
# Open and read csv
with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    

    for row in csv_reader:
        total_vote = total_vote + 1
        votes.append(row[2])

from collections import Counter

candidates = dict(Counter(votes))        
        

total_vote_output = "Total Votes: " + str(total_vote)

output_path = os.path.join('analysis/analysis.txt')
#output_path = '/Users/justinmerryman/Documents/Rice-BootCamp-Homeworks/python_challenge/PyPoll/analysis/analysis.txt'

# Open the file using "write" mode. Specify the variable to hold the contents
file = open(output_path, 'w',)
file.write("Election Results \n")
file.write("------------------------------------- \n")
file.write(total_vote_output)
file.write("\n")
file.write("------------------------------------- \n")


    
    
print("Election Results")
print("--------------------------------------")
print("Total Votes: " + str(total_vote))
print("--------------------------------------")


percent = float(0.001)
for x in candidates:
  names.append(x)


for x in candidates.values():
  cand_votes = float(x)
  totals.append(cand_votes)
  percent = 100 * float(cand_votes) / float(total_vote)
  percent = ("%.3f" % percent)
  percents.append(percent)

num = len(names) 

high = totals[0]
loc = 0

for y in range(num):
  print(names[y]+ ":  " + str(percents[y]) + "%  " + "(" + str(totals[y]) + ")" )
  file.write(names[y]+ ":  " + str(percents[y]) +"%    " + "(" + str(totals[y]) + ")" )
  file.write("\n")
  if totals[y] > high :
    high = totals[y]
    loc = loc + 1

file.write("------------------------------------- \n")
print("--------------------------------------")
file.write("The Winner is: " + names[loc])
file.write("\n")  
print("The Winner is: " + names[loc])
file.write("------------------------------------- \n")
print("--------------------------------------")



















