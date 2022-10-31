import csv

with open('data/domain.csv', "r") as file:
    reader = csv.reader(file)
    headers = next(reader)
    myNames = list(headers)
    print(myNames[0])