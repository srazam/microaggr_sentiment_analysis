'''
    Creating charts across all of the comments of how many BERT incorrectly labeled as hate and non-hate (according to us)
'''

import matplotlib.pyplot as plt
import csv

HtoNH = 0
NHtoH = 0
totalComments = 0

inputs = [Path('.') / 'evaluation' / filename for filename in
         ['eval_AntMan.csv',
          'eval_Aquaman.csv',
          'eval_BlackAdam.csv',
          'eval_BlackPanther.csv',
          'eval_CaptainMarvel.csv',
          'eval_CAWinterSoldier.csv',
          'eval_DoctorStrange.csv',
          'eval_MsMarvel.csv',
          'eval_Pennyworth.csv',
          'eval_ShangChi.csv',
          'eval_SHAZAM.csv',
          'eval_WonderWoman.csv']]

#Caluclate the number of comments that we labeled right and not right
for input in inputs:
    with open(input, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)


        for row in reader:
            bertLabel = row["predicted_label"]
            trueLabel = row["True Label"]
            
            if row.get("predicted_label") and row.get("True Label"):
                totalComments += 1

            if bertLabel == "HATE" and trueLabel == "NON_HATE":
                HtoNH += 1
            elif bertLabel == "NON_HATE" and trueLabel == "HATE":
                NHtoH += 1


# Create the bar chart
categories = ['Incorrectly Labeled Hate', 'Incorrectly Labeled Non-Hate']
values = [HtoNH, NHtoH]

plt.figure(figsize=(12, 6))
bars = plt.barh(categories, values)

plt.xlabel('Count')
plt.ylabel('Label Type')
plt.xlim(0, max(values) * 1.2) 
plt.xticks(range(0, 50, 5)) 


plt.title("BERT Model's Accuracy with Labeling Hate Speech Comments Before Fine-tuning")
caption = 'Note: There is a total of ' + str(totalComments) + ' comments that the model labeled that we labeled'
plt.text(0.5, -0.2, caption, ha='center', va='center', transform=plt.gca().transAxes)

plt.tight_layout()
plt.savefig('../finalGraphs/figure.png')
plt.show()