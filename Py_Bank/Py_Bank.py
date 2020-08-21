import os
import csv

#Accessing the csv file.
bank_data = os.path.join("Resource_Folder","budget_data.csv")
#print(bank_data, type(bank_data))

#Exporting to a text file.
financial_analysis = os.path.join("Analysis_Folder","Financial_Analysis.txt")

#Opening the file as a reader.
#with open(output_path, 'r') as csvfile:
with open(bank_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}"  )

#declaration lists
    month_counter = 0
    profit_total = 0
    diff = 0
    prev_val = 0
    total_diff = 0
    greatest_increase = 0
    greatest_decrease = 0
    great_month = ""
    least_month = ""
    

#for loop for all output components
    for row in csvreader:
        month_counter = (month_counter + 1)
        profit_total = (profit_total + int(row[1]))
        if int(month_counter) != 1:
            diff = (int(row[1]) - int(prev_val))
            if greatest_increase < diff:
                greatest_increase = diff 
                great_month = row[0]
            if greatest_decrease > diff:
                greatest_decrease = diff 
                least_month = row[0]      
        total_diff = (total_diff + diff)
        prev_val= int(row[1])
          
    average_change = total_diff/(month_counter - 1)
    average_change = str(round(average_change, 2))

#Final print statements
Analysis = (
    f"Financial Analysis\n"
    f"-----------------------------\n"
    f"Total Months:   {str(month_counter)}\n"
    f"Total Profit: ${profit_total}\n"
    f"Average Change:  ${average_change}\n"    
    f"Greatest Increase in Profits:  {great_month} ${greatest_increase}\n"
    f"Greatest Decrease in Profits:  {least_month} ${greatest_decrease}\n")

# Open the file using "write" mode. Specify the variable to hold the contents
print(Analysis)
with open(financial_analysis, 'w') as txt_file:

    # Initialize txt.writer
    txt_file.write(Analysis)
    