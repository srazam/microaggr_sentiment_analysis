'''
In this approach, the comments are tokenized, and a Word2Vec model is trained on the tokenized data. 
The Word2Vec model is used to convert each comment into a series of word vectors. These word vectors 
are then flattened into a single vector representation for each comment. Finally, an SVM model is 
trained using these vector representations as input features.

Remember to experiment with different parameter values, such as vector size, window size, and SVM kernel, 
to find the best configuration for your specific task.
'''

import pandas as pd
from gensim.models import Word2Vec
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer

#Load csv file of comments
data = pd.read_csv('comments.csv')

X = data['comment_text']  # Replace 'comment_text' with the actual column name in your CSV file that contains the comments
y = data['label']  # Replace 'label' with the actual column name in your CSV file that contains the labels (bigoted or not bigoted)

#Split data into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tokenize the text data
tokenized_data = X_train.apply(lambda x: x.split())  # Split each comment into a list of words

# Train the Word2Vec model
word2vec_model = Word2Vec(tokenized_data, size=100, window=5, min_count=1, sg=1)  
# Adjust the size, window, min_count, and sg parameters based on your specific requirements

# Transform each comment into a vector representation using the trained Word2Vec model
X_train_w2v = X_train.apply(lambda x: 
                            pd.Series([word2vec_model[word] for word in x.split() if word in word2vec_model.vocab]))
X_test_w2v = X_test.apply(lambda x: 
                          pd.Series([word2vec_model[word] for word in x.split() if word in word2vec_model.vocab]))

#Flattening the word vectors into a single vector representation
X_train_w2v = X_train_w2v.stack().reset_index(level=1, drop=True)
X_test_w2v = X_test_w2v.stack().reset_index(level=1, drop=True)

#Converting text data to numerical representation using TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

#Training the SVM model
svm_model = SVC(kernel='linear')
svm_model.fit(X_train_w2v, y_train)  # You can also use X_train_tfidf instead of X_train_w2v if you prefer using TF-IDF vectors

#Make predicitons on the test set
y_pred = svm_model.predict(X_test_w2v)  # You can also use X_test_tfidf instead of X_test_w2v if you used TF-IDF vectors for training

#Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
