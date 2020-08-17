import os
import csv

#Accessing the csv file.
bank_data = os.path.join(".", "budget_data.csv")
print(bank_data, type(bank_data))

#Opening the file as a reader.
#with open(output_path, 'r') as csvfile:
with open(bank_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    print(f"Header: {csv_header}"  )
    
    for row in csvreader:
           print(row)


#Define the two variables in the document.
def month = row[0]
def profit_loses = row[1] 
    print(month)

#Total count of months (column 1)- will need to do a count of all of the months should equal 86.
       #def Total_Months len(month)
        #print("Total Months: ", Total_Months))

#Total sum of Profit/Losses.  Total the entire column.
        #def Total_Profit sum(profit_loses)
        # print("Total Profit/Loses:  ", Total_Profit))


# Find the average change a month.
        #def Average_Change(Total_Profit/Total_Months) 
        #print("Average Change:  ", Average_Change)

# Find the max profit/Change
        #def max(max_profit):
            #max_so_far = max_profit[0]
            #for profit_loses in profit:
                #if profit_loses < max_so_far:
                    #max_so_far = max_profit
            #return max_profit
            #print("Greatest Increase in Profits:  ", max_profit)

#Find the min profit/Change
        #def min(min_profit):
            #min_so_far = min_profit[0]
            #for number in numbers:
                #if number < min_so_far:
                #min_so_far = number
            #return min_so_far
            #print("Greatest Decrease in Profits:  ", max_profit)