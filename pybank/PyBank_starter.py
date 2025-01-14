# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change = 0
month_list = []
net_change_list = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])


    # Track the total and net change


    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1 # increment total months by 1
        total_net += int(row[1]) # add the current's profit/loss to the total net


        # Track the net change
        net_change = int(row[1]) - previous_net # calculate change from the previous month
        net_change_list.append(net_change) #add the change to the net_chnge_list
        month_list.append(row[0]) #add the month to the month_list
        previous_net = int(row[1]) #update previous_net for the next iteration


        # Calculate the greatest increase in profits (month and amount)
        greatest_increase = max(net_change_list) # find the max net change
        greatest_increase_month = month_list[net_change_list.index(greatest_increase)] #find the corresponding month



        # Calculate the greatest decrease in losses (month and amount)
        greatest_decrease = min(net_change_list) # find the min net change
        greatest_decrease_month = month_list[net_change_list.index(greatest_decrease)] #find the corresponding month





# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list)


# Generate the output summary
output = (
    f"Financial Analysis \n"
    f"total month: {total_months}\n"
    f"total: ${total_net}\n"
    f"average change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (&{greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (&{greatest_decrease})\n"
    )



# Print the output
print(output)


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
