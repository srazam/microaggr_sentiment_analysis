
from happytransformer import HappyTextClassification
from datasets import load_dataset
import csv

def run_finetune():
    train_csv_path = "train.csv"
    eval_csv_path = "eval.csv"

    train_dataset = load_dataset('tweets_hate_speech_detection', split='train[0:1999]')
    eval_dataset = load_dataset('tweets_hate_speech_detection', split='train[2000:2499]')

    generate_csv(train_csv_path, train_dataset)
    generate_csv(eval_csv_path, eval_dataset)

    happy_tc = HappyTextClassification(model_type="BERT", model_name="dehatebert-mono-english", num_labels=2)
    
    before_loss = happy_tc.eval(eval_csv_path)
    happy_tc.train(train_csv_path)
    after_loss = happy_tc.eval(eval_csv_path)

    print("Before loss: ", before_loss.loss)
    print("After loss: ", after_loss.loss)
    
def generate_csv(csv_path, dataset):
    with open(csv_path, 'w', newline='') as csvfile:
        writter = csv.writer(csvfile)
        writter.writerow(["text", "label"])
        for case in dataset:
          text = case["tweet"]
          label = case["label"]
          writter.writerow([text, label])
run_finetune()