# Importing the os module
import os

# Module for reading CSV file
import csv

# Setting path for CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Setting variables
months = 0
total_revenue = 0
change = 0
previous_revenue = 0
greatest_increase = 0
greatest_decrease = 9999999999999999999999
increase_date = ""
decrease_date = ""
revenue_change = []

# Reading into CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    # Defining "data" as list
    data = list(csvreader)
    # "months" = number of items(/months) in data
    months = len(data)
    for row in data: