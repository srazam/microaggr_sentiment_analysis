import matplotlib.pyplot as plt
import csv

inputs = ['something.csv', 'somethingelse.csv']

correct = 0
HtoNH = 0
NHtoH = 0
totalComments = 0


#Caluclate the number of comments that we labeled right and not right
for input in inputs:
    with open(input, 'r') as file:
        reader = csv.DictReader(file)

        #Iterate over each row in the CSV
        for row in reader:

            bertLabel = file["BERT Label"]
            trueLabel = file["True Label"]

        #Compare the values from the two different columns
        if bertLabel == trueLabel:
            correct += 1
        elif bertLabel == "HATE" and trueLabel == "NON_HATE":
            HtoNH += 1
        elif bertLabel == "NON_HATE" and trueLabel == "HATE":
            NHtoH += 1

        totalComments += 1

#Creating the bar chart
categories = ['Correctly Labeled', 'Incorrectly Labeled Hate', 'Incorrectly Labeled Non-Hate']
counts = [correct, HtoNH, NHtoH]

plt.barh(categories, counts)
plt.xlabel('Count')
plt.ylabel('How the Model Labeled the Comment')

plt.title("How Well did the BERT Model Label " + totalComments + " Comments")

plt.show()

