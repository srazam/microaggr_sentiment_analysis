# Applying a word embedding model in order to get vector representations of the words

import pandas as pd
import nltk
from gensim.models import Word2Vec

#Load the CSV file
data = pd.read_csv('thecomments.csv')

# ***Use for preprocessing text***

#Dowload stopwords
nltk.download('stopwords')

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token for token in tokens if token.isalpha()]
    return tokens

#Apply preprocessing to comments
data['preprocessed_comments'] = data['comment'].apply(preprocess_text)

#Train Word2Vec model (min_count specifies minimum frequency of a word to be considered in the model)
model = Word2Vec(data['preprocessed_comments'], min_count=1)

#Access word vectors

#Save the model so you can reuse it in the future
model.save('word2vec_model.bin')

#Put all of the word vectors on a csv file
words = list(model.wv.vocab.keys()) #Get al unique words in the model's vocab
vectors=pd.DataFrame(model.wv[words]) #Create a dataframe to store the word vectors
vectors['word'] = words #Add words as a column in the DataFrame
vectors.to_csv('output.csv', index=False) #Saving the DataFrame to a csv file