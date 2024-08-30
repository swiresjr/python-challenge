import os
import base64
import csv

budget_csv = os.path.join('PyBank','Resources','budget_data.csv') #refernces CSV file

print("Financial Analysis")#prints the title

with open(budget_csv, encoding='UTF-8') as csvfile: #opens CSV file
    csvreader = csv.reader(csvfile) #reads in CSV file
    
    for column in csvreader:
        month_count=(column[0])
        print(f"Total Months: ", str(len(month_count)))




    








