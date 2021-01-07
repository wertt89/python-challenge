# Importing the OS module
import os

# Module for reading CSV file
import csv

# Setting path for CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Setting variables and initial values
months = 0 # Works as number of months and number of rows
profitloss_total = 0 # Sum of Profit/Loss values
profitloss_change = 0 # Change of Profit/Loss from one month to another
next_month_value = 0 # "From" value
previous_month_value = 0 # "To" value
profit_change_sum = 0 # Sum of all Profit/Loss changes
profit_change_average = 0 # Average of profit_change_sum
max_increase = 0
min_increase = 0
increase_date = ""
decrease_date = ""
profitloss_changes = [] # Store monthly profitloss_change

# Reading into CSV file
with open(csvpath) as csvfile:

    # Setting csvreader variable
    csvreader = csv.reader(csvfile)
    next(csvreader,None)
    # Defining data variable that can be referenced
    data = list(csvreader)
    # "months" = number of rows in data
    months = len(data)
    # Looping through data
    for row in data:
        # Finding sum of Protif/Loss column values
        profitloss_total += int(row[1])
        # Calculating change of Profit/Loss to previous row
        next_month_value = int(row[1])
        profitloss_change = next_month_value - previous_month_value  
        # Store monthly Profit/Loss change in a list
        profitloss_changes.append(profitloss_change)
        profit_change_sum = profit_change_sum + profitloss_change
        previous_month_value = next_month_value
        # Calculating average of change by subtracting Jan-2010 value and one month as first month is skipped, then rounding to the nearest hundredth
        profit_change_average = round((profit_change_sum-int(data[0][1]))/(months-1),2)
        # Determining the greatest increase
        if (profitloss_change > max_increase):
            max_increase = profitloss_change
            # print(type(row))
            # print(row)
            increase_date = row[0]
        # Determining the greatest decrease
        if (profitloss_change < min_increase):
            min_increase = profitloss_change
            decrease_date = row[0]

    # Printing all required outputs on separate lines and formatting monetary values to include thousand separators
    print("Financial Analysis" + "\n" + "----------------------------" + "\n" + "Total Months: " + str(months) + "\n" + "Total: $" + f'{profitloss_total:,}' + "\n" + "Average Change: $" + f'{profit_change_average:,}' + "\n" + "Greatest Increase in Profits: " + increase_date + " ($" + f'{max_increase:,}' + ")" + "\n" + "Greatest Decrease in Profits: " + decrease_date + " ($" + f'{min_increase:,}' + ")")

# Creating output file and exporting results to analysis folder
    output_file = 'analysis/results.txt'
    with open(output_file, "w") as txt_file:
        txt_file.write("Financial Analysis")
        txt_file.write("\n----------------------------")
        txt_file.write("\nTotal Months: " + str(months))
        txt_file.write("\nTotal: $" + f'{profitloss_total:,}')
        txt_file.write("\nAverage Change: $" + f'{profit_change_average:,}')
        txt_file.write("\nGreatest Increase in Profits: " + increase_date + " ($" + f'{max_increase:,}' + ")")
        txt_file.write("\nGreatest Decrease in Profits: " + decrease_date + " ($" + f'{min_increase:,}' + ")")