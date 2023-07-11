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

            #Compare the values from the two different columns
            if bertLabel == "HATE" and trueLabel == "NON_HATE":
                HtoNH += 1
                totalComments += 1
            elif bertLabel == "NON_HATE" and trueLabel == "HATE":
                NHtoH += 1
                totalComments += 1

#Creating the bar chart
categories = ['Incorrectly Labeled Hate', 'Incorrectly Labeled Non-Hate']
counts = [HtoNH, NHtoH]

plt.figure(figsize=(8,6))
plt.barh(categories, counts)
plt.xlabel('Count')
plt.ylabel('How the Model Labeled the Comment')

plt.title("How Well did the BERT Model Label " + str(totalComments) + " Comments")

plt.tight_layout()
plt.show()

