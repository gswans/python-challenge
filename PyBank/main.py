# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Model for formating currency
import locale

# csvpath = '../Resources/budget_data.csv'

csvpath = os.path.join('.','Resources', 'budget_data.csv')


#print(csvpath)


# Method: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
   
    # Read each row of data after the header
    #for slamdunk in csvreader:
    #    print(slamdunk)

    # Calculate the total number of months
    print("__________________________________")
    print("Financial Analysis")
    print("__________________________________")

    tot_month=0
    for row in csvreader:
        tot_month=tot_month+1
    print("Total Months: "+str(tot_month))

# Calculate the total profit and loss
    # csvpath = '../Resources/budget_data.csv'

csvpath = os.path.join('.','Resources', 'budget_data.csv')


#print(csvpath)


# Method: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)  
    profit_loss = 0
    for row in csvreader:
        profit_loss+= int(row[1])
    locale.setlocale(locale.LC_ALL, 'en_US.utf-8') 
    #s = locale.currency(profit_loss, grouping=True)
    print("Total: "+str(locale.currency(profit_loss, grouping=True)))
# Method: Creating a list called empty
# Use it to calculate Average change

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    empty = []
    date_val = []
    for row in csvreader:
        empty.append(row[1])
        date_val.append(row[0])
    #print(date_val)
    sum_diff = 0
    for val in range(len(empty) - 1):
        diff = int(empty[val+1]) - int(empty[val]) 
        sum_diff += diff
    ave_diff = sum_diff/(len(empty) -1)
    locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
    print("Average Change: " + str(locale.currency(ave_diff,grouping=True)))

    # Finding the greatest increase in profit
    p_l_change = []
    for val in range(len(empty) - 1):
        diff = int(empty[val+1]) - int(empty[val])
        p_l_change.append(diff) 
    #print(p_l_change)
    # Comparing profit and loss increases
    greatest_inc = max(p_l_change)
    greatest_dec = min(p_l_change)
    #print(greatest_inc)
    #print(greatest_dec)
    del(date_val[0])

    date_P_l_change = zip(p_l_change, date_val)
    date_p_l_results = set(date_P_l_change)
    #print(date_p_l_results)
    max(date_p_l_results)
    min(date_p_l_results)
    print("Greatest Increase in Profits: " + str(max(date_p_l_results)))
    print("Greatest Dcrease in Profits: " + str(min(date_p_l_results)))
print("________________________________________________")
#print(date_val)   
#print(len(p_l_change))
#print(len(date_val))



    