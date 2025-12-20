# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 14:28:40 2025

@author: wendy et eloise 


"""


from matplotlib import pyplot as plt
import math 

filepath = input("afficher les dossiers :")
filepath = [filepath,'csv']
filepath = '.'.join(filepath)




figure, axis = plt.subplots()
        
x=[]
y=[]

mouse_id = "ABX001"

fd = open (filepath, "r")
# skip 1st line
line = fd.readline()
# retrieve 1st data line (2nd line)
line = fd.readline()

while line != '':
    # remove endof line character
    line = line.replace("\n", "")
    data = line.split(";")
    print(data)
    

    if data [4]== mouse_id : 
    
      
        # process only for SECAL samples
        if data[2] == 'fecal':
            x_value = float(data[7])
            y_value = math.log10(float(data[8]))
            x.append(x_value)
            print( "l'axe x :" ,x)
            y.append(y_value)
            print("l'axe y :" ,y)
            

    line = fd.readline()
fd.close()

# draw curve    
axis.plot(x,y)

figure.savefig("out.png", dpi=200)


    
