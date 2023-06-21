import csv
import nltk
import re
import numpy as np
import heapq


input_file = 'C:/Users/AzamF/Documents/GitHub/reuData/GOTGV2_clean.csv'
output_file = 'C:/Users/AzamF/Documents/GitHub/reuData/GOTGV2_bow.csv'
column_index_text = 2 #Column of the clean text 

with open(input_file, 'r', newline='', encoding='utf-8', errors='ignore') as csvfile, open(output_file, 'w', newline='', encoding='utf-8', errors='ignore') as outfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(outfile)

    #Creat bag of words model
    word2count = {}

    for row in reader:
        words = nltk.word_tokenize(row[column_index_text])
        for word in words:
            if word not in word2count.keys():
                word2count[word] = 1
            else:
                word2count[word] += 1

    freq_words = heapq.nlargest(100, word2count, key=word2count.get)

    X = []
    for row in reader:
        vector = []
        for word in freq_words:
            if word in nltk.word_tokenize(row[column_index_text]):
                vector.append(1)
            else:
                vector.append(0)
            X.append(vector)
        X = np.asarray(X)
