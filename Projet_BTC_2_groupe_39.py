# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 14:28:40 2025

@author: wendy et eloise 


"""

from matplotlib import pyplot as plt
import math 

filepath = input("Enter the CSV name file (without extention) :")
filepath = [filepath,'csv']
filepath = '.'.join(filepath)


   
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
        if data[4]==mouse_id :
            if data[2] == 'fecal':
                x_value = float(data[7])
                y_value = math.log10(float(data[8]))
                x.append(x_value)
                y.append(y_value)
                #get color for treatment 
                treatment= data[5]



        line = fd.readline()
    
    fd.close()
    clr = 'blue'
    if treatment == 'ABX':
        clr = 'red'




# draw curve    
    axis.plot(x,y,color = clr, label = treatment)
figure.savefig("out.png", dpi=200)
figure.legend(loc='right')   
axis.text(0.78, 0.95, "Red : Antibiotic (ABX)", color="red", transform=axis.transAxes)
axis.text(0.78, 0.90, "Blue : Placebo", color="blue", transform=axis.transAxes)

    
axis.set_title("Fecal live bacteria")
axis.set_xlabel("log10(live bacteria/wet g)")
axis.set_ylabel("Whashout day")




figure, axis = plt.subplots()
        
cecal_abx = []
cecal_plb = []


fd = open("data_small.csv", "r")
# skip 1st line
line = fd.readline()
# retrieve 1st data line (2nd line)
line = fd.readline()
while line != '':
    # remove endof line character
    line = line.replace("\n", "")
    data = line.split(";")

    # process only for SECAL samples
    if data[2] == 'cecal':
        value = math.log10(float(data[8]))
        if data[5] == 'ABX':
            cecal_abx.append(value)
        else:
            cecal_plb.append(value)

    
    line = fd.readline()
fd.close()
# récupérer les violons
violins = axis.violinplot([cecal_abx, cecal_plb], positions = [ 1,2 ], showmedians=False)

#  appliquer les couleurs
for violin, color in zip(violins['bodies'], ["red", "blue"]):
    violin.set_facecolor(color)

    violin.set_alpha(0.1)
    
# draw curve    
axis.violinplot([cecal_abx, cecal_plb])
figure.savefig("out.png", dpi=200)
    
plt.title("Cecal live bacteria")
plt.xlabel("log10(live bacteria/wet g)")
plt.ylabel("Treatment")
plt.xticks([1, 2],["ABX", "Placebo"])
#legend on top and right
axis.text(0.65, 0.95, "Red : Antibiotic (ABX)", color="red", transform=axis.transAxes)
axis.text(0.65, 0.90, "Blue : Placebo", color="blue", transform=axis.transAxes)

figure, axis = plt.subplots()
  
ileal_abx = []
ileal_plb = []

fd = open("data_small.csv", "r")
# skip 1st line
line = fd.readline()
# retrieve 1st data line (2nd line)
line = fd.readline()
while line != '':
    # remove endof line character
    line = line.replace("\n", "")
    data = line.split(";")
    
    # process only for ILEAL samples    
    if data[2] == 'ileal':
        value = math.log10(float(data[8]))
        if data[5] == 'ABX':
            ileal_abx.append(value)
        else:
            ileal_plb.append(value)
    
    line = fd.readline()
fd.close()


# récupérer les violons

violins = axis.violinplot([ileal_abx, ileal_plb],positions =[1,2], showmedians=False)

# appliquer les couleurs
for violin, color in zip(violins['bodies'], ["red", "blue"]):
    violin.set_facecolor(color)
    violin.set_alpha(0.1)

# draw curve    
plt.title("Ileal live bacteria")
plt.xlabel("log10(live bacteria/wet g)")
plt.ylabel("Treatment")
plt.xticks([1, 2],["ABX", "Placebo"])
#legend on top and right
axis.text(0.65, 0.95, "Red : Antibiotic (ABX)", color="red", transform=axis.transAxes)
axis.text(0.65, 0.90, "Blue : Placebo", color="blue", transform=axis.transAxes)



