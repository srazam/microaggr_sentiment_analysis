import matplotlib.pyplot as plt
import csv

inputs = [r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_BlackPanther.csv', 
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_CaptainMarvel.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_BlackAdam - labeled_BlackAdam.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_MsMarvel - labeled_MsMarvel.csv', 
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_ShangChi - labeled_ShangChi.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_WonderWoman - labeled_WonderWoman.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_AntMan - labeled_AntMan.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_Aquaman - labeled_Aquaman.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_CAWinterSoldier - labeled_CAWinterSoldier.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_DoctorStrange - labeled_DoctorStrange.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_Pennyworth - labeled_Pennyworth.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_SHAZAM - labeled_SHAZAM.csv'
          ]

HtoNH = 0
NHtoH = 0
totalComments = 0


#Caluclate the number of comments that we labeled right and not right
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
            if bertLabel == "HATE" and trueLabel == "NON_HATE":
                HtoNH += 1
            elif bertLabel == "NON_HATE" and trueLabel == "HATE":
                NHtoH += 1

#Creating the bar chart
categories = ['Incorrectly Labeled Hate', 'Incorrectly Labeled Non-Hate']
counts = [HtoNH, NHtoH]

plt.figure(figsize=(12,6))
plt.barh(categories, counts)

plt.xticks(range(0, NHtoH + 1, 5))

plt.xlabel('Count')
plt.ylabel('Label Type')

plt.title("BERT Model's Accuracy with Labeling Hate Speech Comments")

caption = 'Note: There is a total of ' + str(totalComments) + ' comments that the model labeled that we labeled'
plt.text(0.5, -0.2, caption, ha='center', va='center', transform=plt.gca().transAxes)

plt.tight_layout()
plt.show()

