import csv 
from textblob import TextBlob

input_file = r'C:\Users\AzamF\Documents\GitHub\reuData\GOTGV2_6-26.csv'
output_file = r'C:\Users\AzamF\Documents\GitHub\reuData\GOTGV2_polarity.csv'

columns = ['Video ID', 'Comment Text']

rows_to_write = []
with open(input_file, encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for rows in reader:
        row_to_write = {col: rows[col] for col in columns}
        rows_to_write.append(row_to_write)

for row in rows_to_write:
    text = row['Comment Text']
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        row['Label'] = 'positive'
    elif sentiment < 0:
        row['Label'] = 'negative'
    else:
        row['Label'] = 'neutral'

with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=columns + ['Label'])
    writer.writeheader()
    writer.writerows(rows_to_write)