'''
    Performing initial labeling on data before finetuning BERT model
'''

from transformers import pipeline 
import pandas as pd 

model_name = "Hate-speech-CNERG/dehatebert-mono-english"
nlp = pipeline("text-classification", model=model_name)

input_file = "rawData\FILENAMEHERE.csv"  
output_file = "modelResults\FILENAMEHERE.csv"  

max_sequence_length = 512 #Randomly chosen

df = pd.read_csv(input_file)
texts = df["Comment Text"]  

#Truncate text sequences to maximum length 
truncated_texts = [text[:max_sequence_length] for text in texts]
results = nlp(truncated_texts)

df["label"] = [result["label"] for result in results]
df["confidence"] = [result["score"] for result in results]

df.to_csv(output_file, index=False)
