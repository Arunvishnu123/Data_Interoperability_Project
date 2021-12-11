import csv
with open(r'C:\Users\ARUN\OneDrive\Desktop\Data_Interoperability_Project\CSV_Excercises\CSV_Library_Program\download.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)