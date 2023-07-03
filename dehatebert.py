from transformers import pipeline
import pandas as pd
import re

input_file = r"C:\Users\AzamF\Documents\GitHub\reuData\trailerData\Aquaman_6-27.csv"
output_file = r"C:\Users\AzamF\Documents\GitHub\reuData\modelResults\labeled_Aquaman.csv"

data=pd.read_csv(input_file)

texts = data['Comment Text'].tolist()

model_name = "Hate-speech-CNERG/dehatebert-mono-english"
classifier = pipeline("text-classification", model=model_name)

results = classifier(texts)

output_data=[]
for text, result in zip(texts, results):
    label = result["label"]
    confidence = result["score"]
    output_data.append([text, label, confidence])

output_df = pd.DataFrame(output_data, columns=["text", "label", "confidence"])
output_df.to_csv(output_file, index=False)
