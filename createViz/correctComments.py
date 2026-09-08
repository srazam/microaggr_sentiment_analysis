'''
    Creating charts for the minority-led media trailers and non-minoirty-led media trailers for how many labels BERT incorrectly labeled 
'''

import matplotlib.pyplot as plt
import csv

inputs = [Path('.') / 'evaluation' / filename for filename in
         ['eval_BlackAdam.csv',
          'eval_BlackPanther.csv',
          'eval_CaptainMarvel.csv',
          'eval_MsMarvel.csv',
          'eval_ShangChi.csv',
          'eval_WonderWoman.csv']]

totalComments = 0
minorityCorrect = 0
nonMinorityCorrect = 0

#Caluclate the number of comments that were labeled correctly for minority-led media
for input in inputs:
    with open(input, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:

            bertLabel = row["BERT Label"]
            trueLabel = row["True Label"]

            if row.get("BERT Label") and row.get("True Label"):
                totalComments += 1

            if bertLabel == trueLabel:
                minorityCorrect += 1

inputs = [Path('.') / 'evaluation' / filename for filename in
         ['eval_AntMan.csv',
          'eval_Aquaman.csv',
          'eval_CAWinterSoldier.csv',
          'eval_DoctorStrange.csv',
          'eval_Pennyworth.csv',
          'eval_SHAZAM.csv']]

#Caluclate the number of comments that were labeled correctly for nonminority-led media
for input in inputs:
    with open(input, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:

            bertLabel = row["BERT Label"]
            trueLabel = row["True Label"]

            if row.get("BERT Label") and row.get("True Label"):
                totalComments += 1

            if bertLabel == trueLabel:
                nonMinorityCorrect += 1

#Creating bar chart
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
plt.savefig("../finalGraphs/figure3.py")
plt.show()