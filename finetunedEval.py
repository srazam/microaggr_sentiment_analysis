import os
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
import torch

model_path = r"C:\Users\AzamF\Documents\GitHub\reuData\model_directory"
tokenizer_path = r"C:\Users\AzamF\Documents\GitHub\reuData\tokenizer"

model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained(tokenizer_path)


data_folder = r"C:\Users\AzamF\Desktop\trailerData"
output_folder = r"C:\Users\AzamF\Documents\GitHub\reuData\finalEval"

# Get the list of CSV files in the data folder
file_list = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

# Iterate through each file
for file_name in file_list:
    # Read the CSV file
    input_path = os.path.join(data_folder, file_name)
    output_path = os.path.join(output_folder, file_name[:-4] + "_2.csv")

    df = pd.read_csv(input_path)

    # Perform the labeling using the fine-tuned model 
    texts = df["Comment Text"].tolist()
    # Tokenize and encode the text data 
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

    # Assign the predicted labels to the DataFrame
    df["predicted_label"] = predicted_labels

    # Save the labeled DataFrame to a new CSV file
    df.to_csv(output_path, index=False)
