import matplotlib.pyplot as plt
import csv

inputs = [r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_BlackPanther.csv', 
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_CaptainMarvel.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_BlackAdam - labeled_BlackAdam.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_MsMarvel - labeled_MsMarvel.csv', 
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_ShangChi - labeled_ShangChi.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_WonderWoman - labeled_WonderWoman.csv'
          ]

totalComments = 0
minorityCorrect = 0
nonMinorityCorrect = 0

#Caluclate the number of comments that were labeled correctly for minority-led media
for input in inputs:
    with open(input, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        #Iterate over each row in the CSV
        for row in reader:

            bertLabel = row["BERT Label"]
            trueLabel = row["True Label"]

            #Compare the values from the two different columns
            if bertLabel == trueLabel:
                minorityCorrect += 1

inputs = [r'nonminoritylead.csv'
          ]

#Caluclate the number of comments that were labeled correctly for nonminority-led media
for input in inputs:
    with open(input, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        #Iterate over each row in the CSV
        for row in reader:

            bertLabel = row["BERT Label"]
            trueLabel = row["True Label"]

            #Compare the values from the two different columns
            if bertLabel == trueLabel:
                nonMinorityCorrect += 1

#Creating the bar chart
categories = ['Comments from Minority-Led Media Correctly Labeled', 'Comments from NonMinority-Led Media Correctly Labeled']
counts = [minorityCorrect, nonMinorityCorrect]

plt.figure(figsize=(8,6))
plt.barh(categories, counts)
plt.xlabel('Count')
plt.ylabel('Comments')

plt.title("Number of Comments Correctly Labeled per Class (Out of )")

plt.tight_layout()
plt.show()