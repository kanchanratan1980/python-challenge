# python-challenge
python-challenge: PyBank and Pypoll
Overview
this pproject contains two python challenges, PyBank and PyPoll, designed to showcase python
scripting capabilities for data analysis. Both tasks utilize csv data and require generating summary
reports. the scripts process and analyze financial and financial and election data, respectively, and
output the results both to the terminal and text file.

PyBank
objective
Analyze company's financial records to calculate Key metrics fromm a dataset of monthly
"profit/loss".
Input file

Resources/budget_data.csv
.Column: Date,Profit/losses Task

Calculate the total number of month include in the dataset.
Calculate the total amount of profir/losses over the entire period.
Calculate the changes in "profit/losses" over the entire period.
Determine the greatest increase in prifits(date and amount) over the entire period.
Determine the greatest decrease in profits (date and amount) over the entire period.
Output

print the analysis to the terminal.
Save the results in a text file at analysis/budget_analysis.txt.
Sample Output
1 Financial Analysis
Total Months: 86
Total: &22564198
Average Change: &-8311.11
Greatest Increase in profits:Aug-16(&1862002) Greatest Decrease in profits:Feb-14 (&-1825558)

Pypoll
Object Modernize a small town's votes-counting process by analysis election data to determine key
statistics.
Input file

Resources/election_data.csv .Columns: Ballot ID, County,Candidate Task
Calculate the Total number of votes cast.
Create a complete list of candidates who receved votes.
Calculate the percentage of Votes each candidat won.
Calculate the total number of votes each candidate won.
Determine the winner of the election based on the popular vote. Output
Print the analysis to the terminal.
Save the Result in atextfile at analysis/election_analysis.txt.
Sample Output
Election Results

Total Votes: 369711

Charles Casper Stockham: 23.049% (85213) Diana DeGette: 73.812%(272892)
Raymon Anthony Doane: 3.139% (11606)

Winner: Diana DeGette

Requirement
Python 3.x Os Modules and Standard python libraries