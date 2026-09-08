'''
After extracting, preprocess data by removing emojis and punctuation marks. CSV files will be saved in cleanedData folder to be manually labeled.
NOTE: Did not end up using this file in initial testing for we felt that things such as punctuation and emojis could add important contextual information.
'''
import csv
import re
from pathlib import Path

input_files = files = [Path('..') / 'rawData' / filename for filename in
         ['labeled_AntMan.csv',
          'labeled_Aquaman.csv',
          'labeled_BlackAdam.csv',
          'labeled_BlackPanther.csv',
          'labeled_CaptainMarvel.csv',
          'labeled_CAWinterSoldier.csv',
          'labeled_DoctorStrange.csv',
          'labeled_MsMarvel.csv',
          'labeled_Pennyworth.csv',
          'labeled_ShangChi.csv',
          'labeled_SHAZAM.csv',
          'labeled_WonderWoman.csv']]

output_files = [Path('..') / 'cleanedData' / filename for filename in
         ['cleaned_AntMan.csv',
          'cleaned_Aquaman.csv',
          'cleaned_BlackAdam.csv',
          'cleaned_BlackPanther.csv',
          'cleaned_CaptainMarvel.csv',
          'cleaned_CAWinterSoldier.csv',
          'cleaned_DoctorStrange.csv',
          'cleaned_MsMarvel.csv',
          'cleaned_Pennyworth.csv',
          'cleaned_ShangChi.csv',
          'cleaned_SHAZAM.csv',
          'cleaned_WonderWoman.csv']]

def remove_punctuation(comment):
    #Regex pattern to remove punctuation
    pattern = r'[^\w\s]'

    cleaned_comment = re.sub(pattern, '', comment)
    return cleaned_comment

def remove_emojis(comment):
    # Getting all Unicode ranges that deal with emojis
    emoji_patterns = re.compile("["
                               u"\U0001F600-\U0001F64F"  
                               u"\U0001F300-\U0001F5FF"  
                               u"\U0001F680-\U0001F6FF"  
                               u"\U0001F1E0-\U0001F1FF"  
                               u"\U00002500-\U00002BEF"  
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
                               u"\ufe0f"  
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    cleaned_comment = re.sub(emoji_patterns, '', comment)
    return cleaned_comment

column_index_parent = 6 
column_index_text = 5

for input_file, output_file in zip(input_files, output_files):
    with open(input_file, 'r', newline='', encoding='utf-8', errors='ignore') as infile, open(output_file, 'w', newline='', encoding='utf-8', errors='ignore') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        column_names = next(reader) 
        column_names[column_index_text] = 'cleanedData'
        writer.writerow(column_names)

        #Iterate through each row
        for row in reader:
            
            cleaned_cell = row[column_index_text].replace("?:??", "") #Remove timestamps
            cleaned_cell = remove_emojis(row[column_index_text]) #Removing emojis
            cleaned_cell = remove_punctuation(row[column_index_text]) # Removing punctuation marks

            row[column_index_text] = cleaned_cell.lower()

            #Don't include comments that are blank or just say "hi"
            if not row[column_index_parent] and not row[column_index_text] == "hi" and not row[column_index_text] == "":
                writer.writerow(row) 
