'''
    Using the fine-tuned model, label the comments as hate or non hate
'''

import os
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
import torch

model_path = "\model_directory"
tokenizer_path = "\\tokenizer"

model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained(tokenizer_path)

data_folder = ".\modelResults"
output_folder = ".\\finalEval"

file_list = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

for file_name in file_list:
    input_path = os.path.join(data_folder, file_name)
    output_path = os.path.join(output_folder, file_name[:-4] + "_2.csv")

    df = pd.read_csv(input_path)

    # Label using the fine-tuned model 
    texts = df["Comment Text"].tolist()
    inputs = tokenizer(texts, padding=True, truncation=True, max_length=128, return_tensors="pt")
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    # Make predictions with the model
    with torch.no_grad():
        model.eval()
        inputs = {"input_ids": input_ids, "attention_mask": attention_mask}
        outputs = model(**inputs)
        logits = outputs.logits

    predicted_labels = torch.argmax(logits, dim=1).tolist()

    df["predicted_label"] = predicted_labels

    df.to_csv(output_path, index=False)
