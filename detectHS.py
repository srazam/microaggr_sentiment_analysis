from transformers import pipeline
import pandas as pd

model_name = "Hate-speech-CNERG/dehatebert-mono-english"
nlp = pipeline("text-classification", model=model_name)

input_file = r"C:\Users\AzamF\Desktop\trailerData\WakandaForever_6-27.csv"  
output_file = r"C:\Users\AzamF\Documents\GitHub\reuData\modelResults\labeled_WakandaForever.csv"  

max_sequence_length = 512

df = pd.read_csv(input_file)
texts = df["Comment Text"]  

truncated_texts = [text[:max_sequence_length] for text in texts]
results = nlp(truncated_texts)

df["label"] = [result["label"] for result in results]
df["confidence"] = [result["score"] for result in results]

df.to_csv(output_file, index=False)