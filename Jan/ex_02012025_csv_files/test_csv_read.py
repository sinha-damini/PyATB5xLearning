
"""
To find a csv file in folder:
import os

# Specify the directory to search (e.g., current directory)
directory = "C:/Users/HP/PycharmProjects/PyATB5xLearning/Dec"

# Find all CSV files in the directory and subdirectories
csv_files = []
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".csv"):
            csv_files.append(os.path.join(root, file))

# Print the CSV files
print("CSV files found:")
for file in csv_files:
    print(file)

"""

import  csv
import pandas as pd

class Test_READ():
    def test_read_csv(self):
        with open('TestData.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0],row[1])


    def test_read_pandas(self):
        df = pd.read_csv('TestData.csv')
        print(df)