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
    candidate = str(election_data[2])

#Percentage of votes
    #kahan_percent = (khan_counter/total_votes) *100
    #correy_percentage = (correy_counter/total_votes)* 100
    #li_percentage = (li_counter/total_votes)*100
    #otooley_percentage =(otooley_counter/total_votes)*100

#for loop for all output components
    for row in csvreader:
        total_votes = (total_votes + 1)
        if row[2] == "Khan":
            khan_counter = (khan_counter +1)
        if row[2] == "Correy":
            correy_counter = (correy_counter +1)
        if row[2] == "Li":
            li_counter = (li_counter + 1)
        if row[2] == "O'Tooley":
            otooley_counter =( otooley_counter +1)
#Percentage of votes
    khan_percent = format(((khan_counter/total_votes) *100),'.3f')
    correy_percentage = format(((correy_counter/total_votes)* 100),'.3f')
    li_percentage = format(((li_counter/total_votes)*100),'.3f')
    otooley_percentage = format(((otooley_counter/total_votes)*100),'.3f')

 # Determine percent of review left to 2 decimal places
        #percent = round(int(row[6]) / int(row[5]), 2)
        #review_percent.append(percent)

#Final Print Statements
    print(f"Election Results")
    print(f"-----------------------------")
    print(f"Total Votes:   {str(total_votes)}")
    print(f"-----------------------------")
    print(f"Khan: {khan_percent}% ({khan_counter})")
    print(f"Correy: {correy_percentage}% ({correy_counter})")
    print(f"Li: {li_percentage}% ({li_counter})")
    print(f"O'Tooley:  {otooley_percentage}% ({otooley_counter})")
    print(f"-----------------------------")
    