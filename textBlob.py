import csv 
from textblob import TextBlob

input_file = r'C:\Users\AzamF\Documents\GitHub\reuData\GOTGV2_clean.csv'
output_file = r'C:\Users\AzamF\Documents\GitHub\reuData\GOTGV2_polarity.csv'

columns = ['videoId', 'cleanedData']

rows_to_write = []
with open(input_file, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for rows in reader:
        row_to_write = {col: rows[col] for col in columns}
        rows_to_write.append(row_to_write)

for row in rows_to_write:
    text = row['cleanedData']
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        row['sentiment'] = 'positive'
    elif sentiment < 0:
        row['sentiment'] = 'negative'
    else:
        row['sentiment'] = 'neutral'

with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=columns + ['sentiment'])
    writer.writeheader()
    writer.writerows(rows_to_write)