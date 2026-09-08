'''
    Creating a word cloud of common words found in all comments labeled as HATE
'''

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from pathlib import Path

# Downloading resources for tokenizing text and accessing stopword list 
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

files = [Path('.') / 'trueLabels' / filename for filename in
         ['labeled_AntMan.csv',
          'labeled_Aquaman.csv',
          'labeled_BlackAdam.csv',
          'labeled_BlackPanther.csv',
          'labeled_CaptainMarvel.csv',
          'labeled_CAWinterSoldier.csv',
          'labeled_DoctorStrange.csv',
          'labeled_MsMarvel.csv',
          'labeled_Pennyworth.csv',
          'labeled_ShangChi.csv',
          'labeled_SHAZAM.csv',
          'labeled_WonderWoman.csv']]

# Getting all words from hate comments
text_data = ' '
for file in files:
    data = pd.read_csv(file)
    for index, row in data.iterrows():
        if row['True Label'] == 'HATE':
            text_data += row['Comment Text'] + ' '

#Removing stop words
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(text_data)
filtered_text = [word for word in tokens if word.lower() not in stop_words]
filtered_text = ' '.join(filtered_text)

wordcloud = WordCloud(width=800, height=400).generate(text_data)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('finalGraphs/wordCloud.png')
plt.show()