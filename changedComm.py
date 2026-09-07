import matplotlib.pyplot as plt
import csv

HtoNHminority = 0
NHtoHminority = 0

NHtoHnonminority = 0
HtoNHnonminority = 0

totalComments = 0

#Check minority-led media
inputs = [r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_BlackPanther.csv', 
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_CaptainMarvel.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_BlackAdam - labeled_BlackAdam.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_MsMarvel - labeled_MsMarvel.csv', 
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_ShangChi - labeled_ShangChi.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_WonderWoman - labeled_WonderWoman.csv'
          ]

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
                HtoNHminority += 1
            elif bertLabel == "NON_HATE" and trueLabel == "HATE":
                NHtoHminority += 1

#Check minority-led media
inputs = [r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_AntMan - labeled_AntMan.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_Aquaman - labeled_Aquaman.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_CAWinterSoldier - labeled_CAWinterSoldier.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_DoctorStrange - labeled_DoctorStrange.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_Pennyworth - labeled_Pennyworth.csv',
          r'C:\Users\AzamF\Documents\GitHub\reuData\trueLabels\labeled_SHAZAM - labeled_SHAZAM.csv'
          ]


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
                HtoNHnonminority += 1
            elif bertLabel == "NON_HATE" and trueLabel == "HATE":
                NHtoHnonminority += 1

# Create the bar chart
categories = ['Incorrectly Labeled Hate', 'Incorrectly Labeled Hate', 'Incorrectly Labeled Non-Hate', 'Incorrectly Labeled Non-Hate']
values = [HtoNHminority, HtoNHnonminority, NHtoHminority, NHtoHnonminority]
nonminority_color = 'orange'
minority_color = 'blue'
labels = ['Minority', 'Non-Minority']

plt.figure(figsize=(12, 6))
bars = plt.barh(categories, values, color=[minority_color, nonminority_color, minority_color, nonminority_color])

# Set the x-axis label
plt.xlabel('Count')
plt.ylabel('Label Type')

#Change x-axis
plt.xlim(0, max(values) * 1.2) #Adjust upper x-axis limit to 20% more than the largest value
plt.xticks(range(0, 50, 5)) # Show x-axis values from 0 to the maximum vlaue with a step of 5

# Set the chart title and add legend
plt.title("BERT Model's Accuracy with Labeling Hate Speech Comments Before Fine-tuning")
plt.legend(bars, labels)

#Caption
caption = 'Note: There is a total of ' + str(totalComments) + ' comments that the model labeled that we labeled'
plt.text(0.5, -0.2, caption, ha='center', va='center', transform=plt.gca().transAxes)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()