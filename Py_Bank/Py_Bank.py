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
        if int(month_counter) != 1:
            diff = (int(row[1]) - int(prev_val))        
        total_diff = (total_diff + diff)
        prev_val= int(row[1])
    average_change = total_diff/(month_counter - 1)
    average_change = str(round(average_change, 2))
    #This one is not quite right amount is 
    greatest_increase = max(row[1])
    greatest_decrease = (min(row[1]))
    month= (row[0])
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: " + str(month_counter))
    print(f"Total Profit: ${profit_total}" )
    print(f"Average Change:  ${average_change}")    
    print(f"Greatest Increase in Profits:  {month} ${greatest_increase}")
    print(f"Greatest Decrease in Profits:  {month} ${greatest_decrease}")

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
            
            #print("Greatest Decrease in Profits:  ", max_profit)