import csv
import re
#from nltk.tokenize import word_tokenize

#The original file
input_file = 'C:/Users/AzamF/Documents/GitHub/reuData/GOTGV2.csv'
#The cleaned file
output_file = 'C:/Users/AzamF/Documents/GitHub/reuData/GOTGV2_clean.csv'

#Is on a zero-based index
column_index_parent = 6 #Column of the parent Ids 
column_index_text = 2 #Column of the original text 

#Removing punctuation marks
def remove_punctuation(comment):
    #Pattern for removing punctuation mark
    pattern = r'[^\w\s]'

    cleaned_comment = re.sub(pattern, '', comment)
    return cleaned_comment


#Use to remove emojis from the text - emojis are reprsented by specific Unicode ranges so are being matched and then removed 
def remove_emojis(comment):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    cleaned_comment = re.sub(emoji_pattern, '', comment)
    return cleaned_comment

with open(input_file, 'r', newline='', encoding='utf-8', errors='ignore') as csvfile, open(output_file, 'w', newline='', encoding='utf-8', errors='ignore') as outfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(outfile)

    #Taking the first row (the names of each column) and writing it to the new csv file
    column_names = next(reader) 
    column_names[column_index_text] = 'cleanedData'
    writer.writerow(column_names)

    #Iterate through each row
    for row in reader:
        cleaned_cell = row[column_index_text].replace("?:??", "") #Remove timestamps
        cleaned_cell = remove_emojis(row[column_index_text]) #Removing emojis
        cleaned_cell = remove_punctuation(row[column_index_text]) # Removing punctuation marks

        row[column_index_text] = cleaned_cell

        #Make all text lowercase
        row[column_index_text] = row[column_index_text].lower()

        #Removing comments that are replies, blank, or just say "hi"
        if not row[column_index_parent] and not row[column_index_text] == "hi" and not row[column_index_text] == "":
            writer.writerow(row) 
