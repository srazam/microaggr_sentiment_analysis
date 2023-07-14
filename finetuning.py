import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, Dataset
from sklearn.model_selection import train_test_split
import pandas as pd

# Load the dataset into a pandas DataFrame
df = pd.read_csv("C:\Users\AzamF\Documents\GitHub\reuData\sexism_data_modified.csv")  # Modify the filename and path accordingly

# Select the columns for text and label
df = df[["text", "sexist"]]  # Modify the column names accordingly

# Split the dataset into training and validation sets
train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)

class CustomDataset(Dataset):
    def __init__(self, dataframe):
        self.data = dataframe

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        text = self.data.iloc[index]["text"]
        label = self.data.iloc[index]["sexist"]

        return text, label

# Load the BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")  # You can choose a different pre-trained BERT model if needed

# Load the BERT model for sequence classification
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=num_labels)  # Replace `num_labels` with the number of labels in your dataset


