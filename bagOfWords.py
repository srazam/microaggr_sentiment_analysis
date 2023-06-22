import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

input_file = r'C:\Users\AzamF\Documents\GitHub\reuData\GOTGV2_clean.csv'
output_file = r'C:\Users\AzamF\Documents\GitHub\reuData\GOTGV2_bow.csv'

data = pd.read_csv(input_file, encoding='utf-8')

text_column = data['cleanedData']

vectorizer = CountVectorizer()
bag_of_words = vectorizer.fit_transform(text_column)

bag_of_words_array = bag_of_words.toarray()
print(bag_of_words_array)

bag_of_words_df = pd.DataFrame(bag_of_words.toarray(), columns=vectorizer.get_feature_names_out())
bag_of_words_df.to_csv(output_file, index=False, encoding='utf-8')
