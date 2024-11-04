import csv
from collections import Counter

# Path to the input CSV file
file_path = 'Resources/election_data.csv'

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the CSV file
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row
    
    for row in csvreader:
        total_votes += 1  # Count total votes
        candidate = row[2]  # Get the candidate's name
        
        # Count votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate percentages and determine the winner
winner = ''
winning_count = 0
results = []

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Determine the winner
    if votes > winning_count:
        winning_count = votes
        winner = candidate

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results:
    print(result)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results to a text file
with open('analysis/election_results.txt', 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for result in results:
        txtfile.write(result + "\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")