import csv
with open('users.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        print(i)
        u = i[0]
        p = i[1]
        