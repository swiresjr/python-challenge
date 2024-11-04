import os
import base64
import csv
from pathlib import Path

file_path = Path("Resources/budget_data.csv")

# Initialize variables
total_months = 0
total_profit_losses = 0
profit_losses_changes = []
previous_profit_loss = None
greatest_increase = ("", 0)  # (date, amount)
greatest_decrease = ("", 0)  # (date, amount)

# Read the CSV file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])

        # Update total months and total profit/losses
        total_months += 1
        total_profit_losses += profit_loss

        # Calculate change in profit/losses
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            profit_losses_changes.append(change)

            # Check for greatest increase
            if change > greatest_increase[1]:
                greatest_increase = (date, change)

            # Check for greatest decrease
            if change < greatest_decrease[1]:
                greatest_decrease = (date, change)

        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(profit_losses_changes) / len(profit_losses_changes) if profit_losses_changes else 0

 # Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export results to a text file
with open("analysis/financial_analysis.txt", "w") as txtfile:
    txtfile.write("analysis/Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_losses}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")   








