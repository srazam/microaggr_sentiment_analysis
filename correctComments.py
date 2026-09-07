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

            if row.get("BERT Label") and row.get("True Label"):
                totalComments += 1

            #Compare the values from the two different columns
            if bertLabel == trueLabel:
                minorityCorrect += 1

inputs = [r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_AntMan - labeled_AntMan.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_Aquaman - labeled_Aquaman.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_CAWinterSoldier - labeled_CAWinterSoldier.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_DoctorStrange - labeled_DoctorStrange.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_Pennyworth - labeled_Pennyworth.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_SHAZAM - labeled_SHAZAM.csv'
          ]

#Caluclate the number of comments that were labeled correctly for nonminority-led media
for input in inputs:
    with open(input, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        #Iterate over each row in the CSV
        for row in reader:

            bertLabel = row["BERT Label"]
            trueLabel = row["True Label"]

            if row.get("BERT Label") and row.get("True Label"):
                totalComments += 1

            #Compare the values from the two different columns
            if bertLabel == trueLabel:
                nonMinorityCorrect += 1

#Creating the bar chart
categories = ['Minority-Led Media', 'NonMinority-Led Media']
counts = [minorityCorrect, nonMinorityCorrect]
colors = ['blue', 'orange']

plt.figure(figsize=(13,6))
plt.barh(categories, counts, color=colors)

plt.xticks(range(0, nonMinorityCorrect + 1, 100))

plt.xlabel('Count')
plt.ylabel('Number of Comments Correctly Labeled for:')

plt.title("Number of Comments Correctly Labeled per Class Before Fine-tuning")

caption = 'Note: There is a total of ' + str(totalComments) + ' comments that the model labeled that we labeled'
plt.text(0.5, -0.2, caption, ha='center', va='center', transform=plt.gca().transAxes)

plt.tight_layout()
plt.show()