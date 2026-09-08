import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, Dataset
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Get data you will be using to finetune
df = pd.read_csv("sexism_data_modified.csv")  
df = df[["text", "sexist"]] 
label_encoder = LabelEncoder()
df['sexist'] = label_encoder.fit_transform(df["sexist"]) #Label encoding - will turn values in 'sexist' column to 0 or 1
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

# Load the BERT tokenizer and model for sequence classification
tokenizer = BertTokenizer.from_pretrained("Hate-speech-CNERG/dehatebert-mono-english") 
model = BertForSequenceClassification.from_pretrained("Hate-speech-CNERG/dehatebert-mono-english", num_labels=2)

train_dataset = CustomDataset(train_df)
val_dataset = CustomDataset(val_df)

# Tokenize and encode the text data
batch_size = 16
max_length = 128

def tokenize_and_encode(batch):
    texts, labels = zip(*batch)
    inputs = tokenizer.batch_encode_plus(
        list(texts),
        add_special_tokens=True,
        max_length=max_length,
        padding="max_length",
        truncation=True
    )
    input_ids = torch.tensor(inputs["input_ids"])
    attention_mask = torch.tensor(inputs["attention_mask"])
    labels = torch.tensor(labels, dtype=torch.long) 
    return input_ids, attention_mask, labels

# Create data loaders
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, collate_fn=tokenize_and_encode)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, collate_fn=tokenize_and_encode)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Define optimizer and loss function
optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)
loss_fn = torch.nn.CrossEntropyLoss()

#Upload the checkpoint
model = BertForSequenceClassification.from_pretrained("..\model_directory")
tokenizer = BertTokenizer.from_pretrained("..\\tokenizer")

# Fine-tuning loop
num_epochs = 2
for epoch in range(num_epochs):

    model.train()
    train_loss = 0.0
    for batch in train_loader:
        input_ids, attention_mask, labels = batch
        input_ids = input_ids.to(device)
        attention_mask = attention_mask.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        train_loss += loss.item()

        loss.backward()
        optimizer.step()

    # Validation
    model.eval()
    val_loss = 0.0
    total_correct = 0
    total_samples = 0
    with torch.no_grad():
        for batch in val_loader:
            input_ids, attention_mask, labels = batch
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            labels = labels.to(device)

            outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss
            val_loss += loss.item()

            _, predicted_labels = torch.max(outputs.logits, dim=1)
            total_correct += (predicted_labels == labels).sum().item()
            total_samples += labels.size(0)

    train_loss /= len(train_loader)
    val_loss /= len(val_loader)
    accuracy = total_correct / total_samples

    print(f"Epoch {epoch+1}/{num_epochs} - Train Loss: {train_loss:.4f} - Val Loss: {val_loss:.4f} - Val Accuracy: {accuracy:.4f}")

#Save the final model and tokenizer 
model.save_pretrained("..\model_directory")
tokenizer.save_pretrained("..\\tokenizer")

