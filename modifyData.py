import csv

with open(r'C:\Users\AzamF\Documents\GitHub\reuData\sexism_data - sexism_data.csv', 'r', encoding ='UTF-8') as file:
    reader = csv.reader(file)

    header = next(reader)
    column_index = header.index('sexist')
    rows = []

    for row in reader:
        if row[column_index] == 'FALSE':
            row[column_index] = 'NON_HATE'
        elif row[column_index] == 'TRUE':
            row[column_index] = 'HATE'

        rows.append(row)

with open(r'C:\Users\AzamF\Documents\GitHub\reuData\sexism_data_modified.csv', 'w', newline='', encoding='UTF-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)
