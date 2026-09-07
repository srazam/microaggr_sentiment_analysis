import pandas as pd
import os
import csv
import matplotlib.pyplot as plt

nonminority = ["Pennyworth_6-27_2.csv", "Peacemaker_6-26_2.csv", "ThePenguin_6-27_2.csv", "SHAZAM!FOTG_6-26_2.csv", "AntMan_6-27_2.csv", 
               "CAWinterSoldier_6-27_2.csv", "Flash_6-27_2.csv", "SpidermanHomecoming_6-27_2.csv", "DoctorStrange_6-27_2.csv", 
               "AntMan&theWasp_6-27_2.csv", "AntMan&theWaspQuantumania_6-27_2.csv", "SHAZAM!_6-27_2.csv", "ThorRagnarok_6-27_2.csv", 
               "ThorLove&Thunder_6-27_2.csv", "Aquaman_6-27_2.csv", "DSMultiverseofMadness_6-27_2.csv", "TheBatman_6-27_2.csv", 
               "SpidermanFarFromHome_6-27_2.csv", "SpidermanNoWayHome_6-27_2.csv"]
minority = ["SwampThing_6-27_2.csv", "BlackAdam_6-27_2.csv", "WonderWoman_6-27_2.csv", "SecretInvasion_6-27_2.csv", "BlueBeetle_6-27_2.csv", 
            "ShangChi_6-27_2.csv", "BlackWidow_6-27_2.csv", "Loki_6-27_2.csv", "She-Hulk_6-27_2.csv", "WakandaForever_6-27_2.csv", "MoonKnight_6-27_2.csv",
            "BlackPanther_6-27_2.csv", "MsMarvel_6-27_2.csv", "WW1984_6-27_2.csv", "CaptainMarvel_6-27_2.csv"]

folder_path = r"C:\Users\AzamF\Documents\GitHub\reuData\finalEval"
hateNM = 0
non_hateNM = 0

hateM = 0
non_hateM = 0

for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            if any(media == file_name for media in nonminority):
                for row in csv_reader:
                    if row["predicted_label"] == "0":
                        hateNM += 1
                    elif row["predicted_label"] == "1":
                        non_hateNM += 1
            elif any(media == file_name for media in minority):
                for row in csv_reader:
                    if row["predicted_label"] == "0":
                        hateM += 1
                    elif row["predicted_label"] == "1":
                        non_hateM += 1
                
# Create pie chart for minority led media
labels_minority = ['Hate', 'Non-hate']
sizes_minority = [hateM, non_hateM]
colors_minority = ['#ff9999', '#66b3ff']

# Create pie chart for nonminority led media
labels_nonminority = ['Hate', 'Non-hate']
sizes_nonminority = [hateNM, non_hateNM]
colors_nonminority = ['#ff9999', '#66b3ff']

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 5))

# Plot the first pie chart for minority led media
ax1.pie(sizes_minority, colors=colors_minority, labels=labels_minority, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
ax1.set_title('Minority-Led Media')
ax1.text(-1, -1.5, 'Note: There are a total of ' + str(hateM + non_hateM) + " comments extracted from minority-led media", fontsize=8, ha='left')

# Plot the second pie chart for nonminority led media
ax2.pie(sizes_nonminority, colors=colors_nonminority, labels=labels_nonminority, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
ax2.set_title('Nonminority-Led Media')
ax2.text(-1, -1.5, 'Note: There are a total of ' + str(hateNM + non_hateNM) + " comments extracted from nonminority-led media", fontsize=8, ha='left')

# Adjust spacing between subplots
plt.subplots_adjust(wspace=0.3)

# Display the figure
plt.show()
