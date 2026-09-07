import matplotlib.pyplot as plt
import csv

HtoNH = 0
NHtoH = 0

totalComments = 0

inputs = [r'C:\Users\AzamF\Documents\GitHub\reuData\evaluation\labeled_BlackPanther2.csv', 
          r'C:\Users\AzamF\Documents\GitHub\reuData\evaluation\labeled_CaptainMarvel2.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\evaluation\labeled_BlackAdam - labeled_BlackAdam2.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\evaluation\labeled_MsMarvel - labeled_MsMarvel2.csv', 
          r'C:\Users\AzamF\Documents\GitHub\reuData\evaluation\labeled_ShangChi - labeled_ShangChi2.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\evaluation\labeled_WonderWoman - labeled_WonderWoman2.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\evaluation\labeled_AntMan - labeled_AntMan2.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\evaluation\labeled_Aquaman - labeled_Aquaman2.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\evaluation\labeled_CAWinterSoldier - labeled_CAWinterSoldier2.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\evaluation\labeled_DoctorStrange - labeled_DoctorStrange2.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\evaluation\labeled_Pennyworth - labeled_Pennyworth2.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\evaluation\labeled_SHAZAM - labeled_SHAZAM2.csv'
          ]

#Caluclate the number of comments that we labeled right and not right
for input in inputs:
    with open(input, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        #Iterate over each row in the CSV
        for row in reader:

            bertLabel = row["predicted_label"]
            trueLabel = row["True Label"]

            if row.get("predicted_label") and row.get("True Label"):
                totalComments += 1

            #Compare the values from the two different columns
            if bertLabel == "HATE" and trueLabel == "NON_HATE":
                HtoNH += 1
            elif bertLabel == "NON_HATE" and trueLabel == "HATE":
                NHtoH += 1


# Create the bar chart
categories = ['Incorrectly Labeled Hate', 'Incorrectly Labeled Non-Hate']
values = [HtoNH, NHtoH]

plt.figure(figsize=(12, 6))
bars = plt.barh(categories, values)

# Set the x-axis label
plt.xlabel('Count')
plt.ylabel('Label Type')

#Change x-axis
plt.xlim(0, max(values) * 1.2) #Adjust upper x-axis limit to 20% more than the largest value
plt.xticks(range(0, 50, 5)) # Show x-axis values from 0 to the maximum vlaue with a step of 5

# Set the chart title and add legend
plt.title("BERT Model's Accuracy with Labeling Hate Speech Comments Before Fine-tuning")

#Caption
caption = 'Note: There is a total of ' + str(totalComments) + ' comments that the model labeled that we labeled'
plt.text(0.5, -0.2, caption, ha='center', va='center', transform=plt.gca().transAxes)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()