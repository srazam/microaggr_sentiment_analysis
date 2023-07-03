from transformers import pipeline
import pandas as pd
import re

#Put name of file in the input_file 
input_file = r"C:\Users\AzamF\Desktop\trailerData\AntMan_6-27.csv"
output_file = r"C:\Users\AzamF\Documents\GitHub\reuData\modelResults\labeled_WW1984.csv"

data=pd.read_csv(input_file)
data["Comment Text"] = data["Comment Text"].str.lower()
data["Comment Text"] = data["Comment Text"].apply(lambda x: re.sub(r'[^\w\s]', '', x))
texts = data['Comment Text'].tolist()

# Step 1: Load the model
model_name = "Hate-speech-CNERG/dehatebert-mono-english"
classifier = pipeline("text-classification", model=model_name)

# Step 2: Classify text
results = classifier(texts)

# Step 3: Interpret the result
output_data=[]
for text, result in zip(texts, results):
    label = result["label"]
    confidence = result["score"]
    output_data.append([text, label, confidence])

output_df = pd.DataFrame(output_data, columns=["text", "label", "confidence"])
output_df.to_csv(output_file, index=False)
