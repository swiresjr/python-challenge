import os
import base64
import csv

budget_csv = os.path.join('..', 'Resources', 'budget_data.csv') #refernces CSV file

print("Financial Analysis")#prints the title

def print_data(financial_data):#defines function and CSV array
    date = str(financial_data[0])#identifies month column in CSV
    profit_loss = int(financial_data[1])#identifies proft/loss column in CSV
    








