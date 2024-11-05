# Python Challenge: PyBank and PyPoll Analysis

This project contains Python scripts to analyze financial and election data for the **PyBank** and **PyPoll** challenges. Each script processes large CSV datasets, calculates key metrics, and outputs the results to both the terminal and a text file.

## Project Structure

- **PyBank**: Analyzes financial records from `budget_data.csv` to calculate:
  - Total Months
  - Total Profit/Loss
  - Average Change in Profit/Loss
  - Greatest Increase in Profits (month and amount)
  - Greatest Decrease in Profits (month and amount)

- **PyPoll**: Analyzes election data from `election_data.csv` to calculate:
  - Total Votes
  - Vote percentage and total votes for each candidate
  - Election Winner based on popular vote

## Files

- **PyBank**:
  - `pybank_main.py`: Python script for financial analysis.
  - `Resources/budget_data.csv`: Dataset containing monthly profit/loss data.
  - `analysis/budget_analysis.txt`: Output summary of analysis results.

- **PyPoll**:
  - `pypoll_main.py`: Python script for election analysis.
  - `Resources/election_data.csv`: Dataset containing election vote data.
  - `analysis/election_analysis.txt`: Output summary of election results.

## Usage

1. Run each script in the terminal:
   - `python3 PyBank/pybank_main.py`
   - `python3 PyPoll/pypoll_main.py`
2. Results will be displayed in the terminal and saved to the respective `.txt` files in the `analysis` folders.

## Troubleshooting

This project I utilized **ChatGPT** for troubleshooting terminal issues and to clarify the code structure. The final scripts were tested to ensure consistent output and error-free execution. I also utilized ChatGPT to help format this markdown file.

## Requirements Met

- CSV data is read successfully in both PyBank and PyPoll scripts.
- Results are accurately calculated and output to the terminal and text files.
- Code is clean, commented, and meets assignment guidelines.
