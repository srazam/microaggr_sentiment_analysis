#Use for calculating the views to like ratio

import pandas as pd

#Read csv file into a pandas DataFrame
df = pd.read_csv(r'C:\Users\AzamF\Documents\GitHub\reuData\Superhero Movie Trailer Statistics - Sheet2.csv')

#Calculate ratio of views to comments
df['Ratio'] = df['viewCount'] / df['commentCount']

#Save the DataFram with the added column back the the same CSV file
df.to_csv(r'C:\Users\AzamF\Documents\GitHub\reuData\Superhero Movie Trailer Statistics - Sheet2.csv', index=False)