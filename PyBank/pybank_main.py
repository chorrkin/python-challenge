import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank", "Resources", "budget_data.csv")
file_to_output = os.path.join("PyBank", "analysis", "budget_analysis.txt")


# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []
previous_profit = None
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

print("Starting the script...")  # Debugging statement

# Open and read the csv
with open(file_to_load) as financial_data:
    print("File opened successfully")
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
    print("Header skipped")  # Confirm header is skipped

    # Extract the first row to initialize `previous_profit`
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_profit = int(first_row[1])

    # Process each row of data
    for row in reader:
        # Update total months and net total
        total_months += 1
        current_profit = int(row[1])
        total_net += current_profit

        # Calculate the monthly change and append to net_change_list
        net_change = current_profit - previous_profit
        net_change_list.append(net_change)
        previous_profit = current_profit
        print(f"First row processed: Total Months = {total_months}, Total Net = {total_net}")  # Debugging statement


        # Check for greatest increase in profits
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change]

        # Check for greatest decrease in profits
        if net_change < greatest_decrease[1]:
            greatest_decrease = [row[0], net_change]
    print("Finished processing all rows")  # Debugging statement


# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list) if net_change_list else 0
print(f"Average change calculated: {average_change}")  # Debugging statement


# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

print("Script started")
print(f"Total Months after first row: {total_months}")
print(f"Total Net after first row: {total_net}")


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
print("Output written to file")  # Debugging statement
