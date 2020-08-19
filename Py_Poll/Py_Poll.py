import os
import csv

#Accessing the csv file.
election_data = os.path.join("..","Py_Poll","Resources","election_data.csv")
print(election_data, type(election_data))

#Exporting to a text file.
election_results = os.path.join("Election_Results","Election_Results.txt")

#with open(output_path, 'r') as csvfile:
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}"  )

#declaration lists
    khan_counter = 0
    correy_counter = 0
    li_counter = 0
    otooley_counter = 0  
    total_votes = 0

#for loop for all output components
    for row in csvreader:
        total_votes = (total_votes + 1)  


#Final Print Statements
    print(f"Election Results")
    print(f"-----------------------------")
    print(f"Total Votes:   {str(total_votes)}")