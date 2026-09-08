'''
    Creating charts for the minority-led media trailers and non-minoirty-led media trailers for how many labels BERT incorrectly labeled 
'''
import matplotlib.pyplot as plt
import csv

HtoNHminority = 0
NHtoHminority = 0

NHtoHnonminority = 0
HtoNHnonminority = 0

totalComments = 0

#Check minority-led media
inputs = [Path('.') / 'evaluation' / filename for filename in
         ['eval_BlackAdam.csv',
          'eval_BlackPanther.csv',
          'eval_CaptainMarvel.csv',
          'eval_MsMarvel.csv',
          'eval_ShangChi.csv',
          'eval_WonderWoman.csv']]

for input in inputs:
    with open(input, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:

            bertLabel = row["BERT Label"]
            trueLabel = row["True Label"]

            if row.get("BERT Label") and row.get("True Label"):
                totalComments += 1

            if bertLabel == "HATE" and trueLabel == "NON_HATE":
                HtoNHminority += 1
            elif bertLabel == "NON_HATE" and trueLabel == "HATE":
                NHtoHminority += 1

#Check non-minority-led media
inputs = [Path('.') / 'evaluation' / filename for filename in
         ['eval_AntMan.csv',
          'eval_Aquaman.csv',
          'eval_CAWinterSoldier.csv',
          'eval_DoctorStrange.csv',
          'eval_Pennyworth.csv',
          'eval_SHAZAM.csv']]


for input in inputs:
    with open(input, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:

            bertLabel = row["BERT Label"]
            trueLabel = row["True Label"]

            if row.get("BERT Label") and row.get("True Label"):
                totalComments += 1

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


plt.xlabel('Count')
plt.ylabel('Label Type')
plt.xlim(0, max(values) * 1.2) 
plt.xticks(range(0, 50, 5)) 


plt.title("BERT Model's Accuracy with Labeling Hate Speech Comments Before Fine-tuning")
plt.legend(bars, labels)
caption = 'Note: There is a total of ' + str(totalComments) + ' comments that the model labeled that we labeled'
plt.text(0.5, -0.2, caption, ha='center', va='center', transform=plt.gca().transAxes)

plt.tight_layout()
plt.savefig("../finalGraphs/figure2.py")
plt.show()