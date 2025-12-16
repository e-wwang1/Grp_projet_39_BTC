# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 14:28:40 2025

@author: wendy et eloise 


"""
filepath = input("afficher les dossiers :")
filepath = [filepath,'csv']
filepath = '.'.join(filepath)
print (filepath)


def displayFile (filepath) : 
    # open in read-only mode 
    fd = open(filepath, 'r')
    
    #retrieve the next line 
    line = fd.readline()
    
    while line != '': 
        # retrieve one line
        line = fd.readline()
        #remove the new_line character 
        line = line.replace('\n', '')
        
        print (line)
    fd.close()
        
displayFile (filepath)
    
''' from matplotlib import pyplot as plt
 import math   
    
figure, axes = plt.subplots()


N_mouse = 16
for i in range(1,N_mouse +1):
    mouse_id = '00'+ str(i)
    mouse_id = mouse_id[-3:]
    mouse_id = 'ABX'+ mouse_id
    treatment = '?'
    x = []
    y = []
    fp = open('data_small.csv')
    #remove 1st line
    line = fp.readline()
    #get read 1st data line
    line = fp.readline()
    while line != '':
        line = line.replace('\n','')
        data = line.split(';')
        if len(data) == 11:
            #process to retreive mouse data
            if data[4] == mouse_id:
                vx = int(data[7])
                vy = math.log10(float(data[8]))
                print(line)
                #add into x and y
                x.append(vx)
                y.append(vy)
                #retrieve treatment
                treatment = data[5]
                
            #get next line
        line = fp.readline()
fp.close()
clr = 'blue'
if treatment == 'ABX':
    clr = 'green'

axes.plot(x,y,label = mouse_id,color = clr,alpha=0.5)

figure.legend(loc='right')
figure.savefig("out.png", dpi=150)


print(figure)
print(axes)
'''
