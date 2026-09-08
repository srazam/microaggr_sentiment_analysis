'''
    Modifying this sexism data set (from the "Call me sexist but' Dataset [https://search.gesis.org/research_data/SDN-10.7802-2251?doi=10.7802/2251] ) 
    to fit how we labeled our data (i.e. False to Non Hate and True to Hate) so that we can fine-tune our BERT model
'''

import csv
from pathlib import Path

with open('sexism_data_og.csv', 'r', encoding ='UTF-8') as file:
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

with open('sexism_data_modified2.csv', 'w', newline='', encoding='UTF-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)
