import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text_data = ' '

files = [r'something.csv',
         r'somethingelse.csv']

#load data from the csv file
data = pd.read_csv('thefile.csv')

#generate the word cloud from a specific column
for index, row in data.iterrows():
    if data['True Label'] == 'HATE':
        text_data += row['Column Text'] + ' '

wordcloud = WordCloud(width=800, height=400).generate(text_data)

#display word cloud
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()