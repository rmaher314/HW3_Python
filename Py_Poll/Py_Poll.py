import os
import csv

#Accessing the csv file.
election_data = os.path.join("..","Py_Poll", "election_data.csv")
print(election_data, type(election_data))

#with open(output_path, 'r') as csvfile:
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    print(f"Header: {csv_header}"  )