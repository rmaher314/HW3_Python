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

#Counting the number of months and total
    month_counter = 0
    profit_total = 0
    diff = 0
    prev_val = 0
    total_diff = 0
    
#for reader 
    for row in csvreader:
        month_counter = (month_counter + 1)
        profit_total = (profit_total + int(row[1]))
        if month_counter != 1:
            diff = (int(row[1]) - int(prev_val))
        total_diff = (total_diff + diff)
        prev_val= int(row[1])
    average_change = total_diff/month_counter
    print(f"Total Months: " + str(month_counter))
    print(f"Total Profit: {profit_total}" )
    print(f"Average Change:  {average_change}")    

#Define the two variables in the document.
#def month = row[0]
#def profit_loses = row[1] 
    #print(month)

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