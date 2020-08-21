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
    most_votes = 0
    winner = ""

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

 # Determine the winner:
    most_votes = khan_counter
    winner = "Khan"
    if most_votes < correy_counter:
        most_votes = correy_counter
        winner = "Correy"
    if most_votes < li_counter:
        most_votes = li_counter
        winner = "Li"
    if most_votes < otooley_counter:
        most_votes = otooley_counter
        winner = "O'Tooley"

#Final Print Statements
Results = (
    f"Election Results\n"
    f"-----------------------------\n"
    f"Total Votes:   {str(total_votes)}\n"
    f"-----------------------------\n"
    f"Khan: {khan_percent}% ({khan_counter})\n"
    f"Correy: {correy_percentage}% ({correy_counter})\n"
    f"Li: {li_percentage}% ({li_counter})\n"
    f"O'Tooley:  {otooley_percentage}% ({otooley_counter})\n"
    f"-----------------------------\n"
    f"Winner: {winner}\n"
    f"-----------------------------\n")


# Open the file using "write" mode. Specify the variable to hold the contents
print(Results)
with open(election_results, 'w') as txt_file:

    # Initialize txt.writer
    txt_file.write(Results)