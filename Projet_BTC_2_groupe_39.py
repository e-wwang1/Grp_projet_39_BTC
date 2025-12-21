# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 14:28:40 2025

@author: wendy et eloise 


"""

import os
import math
import csv
import shutil
from matplotlib import pyplot as plt
from matplotlib.patches import Patch




# Create folders input ; output ; images 

os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)
os.makedirs("images", exist_ok=True)


#Read input file name and build CSV path

filepath = input("Enter the CSV name file (without extention) :")
filepath = [filepath,'csv']
filepath = '.'.join(filepath)

# Copy CSV in the folder input
csv_name = os.path.basename(filepath)
dest_csv = os.path.join("input", csv_name)
shutil.copy(filepath, dest_csv)


filepath = dest_csv

# -----------------------------
##Create a list of unique mouse IDs

  
mouse_list = []

fd = open(filepath, "r")

#skip 1st line
line = fd.readline()
#retrieve 1st data line (2nd line)
line = fd.readline()

while line != "":
    line = line.replace("\n", "")
    data = line.split(";")
    
    mouse_id = data[4]
    if mouse_id not in mouse_list:
        mouse_list.append(mouse_id)


    line = fd.readline()

fd.close()

# -----------------------------
#Plot fecal samples for each mouse



figure, axis = plt.subplots()
# for 'output' folder
fecal_rows = []
for mouse_id in mouse_list : 

    x=[]
    y=[]
    fd = open(filepath, "r")

    #skip 1st line
    line = fd.readline()
    #retrieve 1st data line (2nd line)
    line = fd.readline()
 
    while line != "":
        line = line.replace("\n", "")
        data = line.split(";")

        # Select data for the current mouse and fecal samples only
        if data[4]==mouse_id :
            if data[2] == 'fecal':
                x_value = float(data[7])
                y_value = math.log10(float(data[8]))
                x.append(x_value)
                y.append(y_value)
                ## Retrieve treatment type
                treatment= data[5]
                fecal_rows.append([mouse_id, x_value, y_value, treatment])
                
        line = fd.readline()
    
    fd.close()
    # Set curve color according to treatment
    clr = 'blue'
    if treatment == 'ABX':
        clr = 'red'
        
# Plot curve    

    axis.plot(x,y,color = clr)

      
 #Figure title, labels, and legend
legend_element =[
    Patch(facecolor='red',label="ABX", alpha=0.7),
    Patch(facecolor='blue',alpha=0.7, label="Placebo")]  
   
axis.set_title("Fecal live bacteria")
axis.set_xlabel("Whashout day")
axis.set_ylabel("log10(live bacteria/wet g") 
plt.legend(handles=legend_element, loc='lower left')

figure.savefig("images/fecal_plot.png", dpi=200)


# safeguard CSV FECAL
with open("output/fecal_data.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["mouse_id","experimental_day","counts_live_bacteria_per_wet_g", "treatment"])
    writer.writerows(fecal_rows)



# -----------------------------
####### CECAL samples:



figure, axis = plt.subplots()
        
cecal_abx = []
cecal_plb = []

fd = open(filepath, "r")
# skip 1st line
line = fd.readline()
# retrieve 1st data line (2nd line)
line = fd.readline()
while line != '':
    # remove end-of-line character
    line = line.replace("\n", "")
    data = line.split(";")

    # process only for cecal samples
    if data[2] == 'cecal':
        value = math.log10(float(data[8]))
        if data[5] == 'ABX':
            cecal_abx.append(value)
        else:
            cecal_plb.append(value)

    
    line = fd.readline()
fd.close()
#draw violin plots
violins = axis.violinplot([cecal_abx, cecal_plb], positions = [ 1,2 ], showmedians=False, showmeans =False)

#  apply colors to violins
for violin, color in zip(violins['bodies'], ["red", "blue"]):
    violin.set_facecolor(color)

    violin.set_alpha(0.1)

# title, labels and legend 
legend_element =[
    Patch(facecolor='red',label="ABX", alpha=0.1),
    Patch(facecolor='blue',alpha=0.1, label="Placebo")]    


plt.title("Cecal live bacteria")
plt.xlabel("Treatment")
plt.ylabel("log10(live bacteria/wet g)")
plt.legend(handles=legend_element, loc='lower right')

figure.savefig("images/cecal_plot.png", dpi=200)

# safeguard CSV
with open("output/cecal_data.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["sample_type", "treatment", "counts_live_bacteria_per_wet_g"])
    for v in cecal_abx:
        writer.writerow(["cecal", "ABX", v])
    for v in cecal_plb:
        writer.writerow(["cecal", "Placebo", v])
        
# -----------------------------   
#######  ILEAL samples

figure, axis = plt.subplots()
  
ileal_abx = []
ileal_plb = []

fd = open(filepath, "r")
# skip 1st line
line = fd.readline()
# retrieve 1st data line (2nd line)
line = fd.readline()
while line != '':
    # remove end-of-line character
    line = line.replace("\n", "")
    data = line.split(";")
    
    # process only ileal samples    
    if data[2] == 'ileal':
        value = math.log10(float(data[8]))
        if data[5] == 'ABX':
            ileal_abx.append(value)
        else:
            ileal_plb.append(value)
    
    line = fd.readline()
fd.close()


# draw violin plots

violins = axis.violinplot([ileal_abx, ileal_plb], showmedians=False, showmeans =False)

# apply volors to violins
for violin, color in zip(violins['bodies'], ["red", "blue"]):
    violin.set_facecolor(color)
    violin.set_alpha(0.1)

   

# Title, labels and legend 
legend_element =[
    Patch(facecolor='red',label="ABX", alpha=0.1),
    Patch(facecolor='blue',alpha=0.1, label="Placebo")]    

plt.title("Ileal live bacteria")
plt.xlabel("Treatment")
plt.ylabel("log10(live bacteria/wet g)")

plt.legend(handles=legend_element, loc='lower right')

figure.savefig("images/ileal_plot.png", dpi=200) 

# Safeguard CSV
with open("output/ileal_data.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["sample_type", "treatment", "counts_live_bacteria_per_wet_g"])
    for v in ileal_abx:
        writer.writerow(["ileal", "ABX", v])
    for v in ileal_plb:
        writer.writerow(["ileal", "Placebo", v])


