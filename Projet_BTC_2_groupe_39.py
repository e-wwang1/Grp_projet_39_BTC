# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 14:28:40 2025

@author: wendy et eloise 


"""

from matplotlib import pyplot as plt
from matplotlib.patches import Patch
import math 

#Read input file name and build CSV path
filepath = input("Enter the CSV name file (without extention) :")
filepath = [filepath,'csv']
filepath = '.'.join(filepath)

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

#Plot fecal samples for each mouse

figure, axis = plt.subplots()

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

        line = fd.readline()
    
    fd.close()
    # Set curve color according to treatment
    clr = 'blue'
    if treatment == 'ABX':
        clr = 'red'

# Plot curve    
    axis.plot(x,y,color = clr)
figure.savefig("out.png", dpi=200)
      
 #Figure title, labels, and legend
legend_element =[
    Patch(facecolor='red',label="ABX", alpha=0.7),
    Patch(facecolor='blue',alpha=0.7, label="Placebo")]  
   
axis.set_title("Fecal live bacteria")
axis.set_xlabel("log10(live bacteria/wet g)")
axis.set_ylabel("Whashout day") 
plt.legend(handles=legend_element, loc='lower left')



####### CECAL samples:

figure, axis = plt.subplots()
        
cecal_abx = []
cecal_plb = []

fd = open("data_small.csv", "r")
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
plt.xlabel("log10(live bacteria/wet g)")
plt.ylabel("Treatment")
plt.legend(handles=legend_element, loc='lower right')

#######  ILEAL samples

figure, axis = plt.subplots()
  
ileal_abx = []
ileal_plb = []

fd = open("data_small.csv", "r")
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
plt.xlabel("log10(live bacteria/wet g)")
plt.ylabel("Treatment")

plt.legend(handles=legend_element, loc='lower right')



