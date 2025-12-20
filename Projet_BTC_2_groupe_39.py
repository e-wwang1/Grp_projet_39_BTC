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
        clr = 'green'




# draw curve    
    axis.plot(x,y,label = mouse_id,color = clr,alpha=0.5)
figure.savefig("out.png", dpi=200)
figure.legend(loc='right')        
    
