# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 10:50:49 2022

@author: kguye
"""

import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib is the most commonly used plotting package in python
While there are several ways to plot in matplotlib, matplotlib.pyplot.plot is the most common

As "matplotlib.pyplot" is most frequently imported as plt as shown above, this gets 
abbreviated as plt.plot()

Required input: plt.plot(x_data,y_data)
Additional optional input can be found online

Here we will build some random datasets and plot them
"""

# #First we'll create a linear set of points between 0 and 1 using numpy.linspace#
# #np.linsapce(start,stop,num_points)#
# #So we'll got between 0, 20, by 100 points#
# x_data = np.linspace(0,20,100)

# #and check the data in the counsole
# # print(x_data)

# #now using the data set of 100 points, we'll input into a sine wave#
# y_data = np.sin(x_data)

# ##To visual the plot a line plot: first call a new figure as plt.figure()##
# ##figures can be assigned numbers if you want to add to the same plot later
# plt.figure(1)
# plt.plot(x_data,y_data)

# #Now we'll make a cosine wave
# y_data_2 = np.cos(x_data)

# #and instead of a line plot, we can plot as a scatter plot using a different marker
# plt.figure(1)
# plt.plot(x_data,y_data_2,marker = 'o')

# #what if we don't want the line connecting the points? two options
# #continue using plt.plot() and make the linewidth (lw) = 0
# plt.figure(2)
# plt.plot(x_data,y_data,marker = 'o',lw = 0)
# ##or use plt.scatter
# plt.figure(2)
# plt.scatter(x_data,y_data_2)

# ## however notice that now both the sine and cosine plots are blue
# ## default matplotlib has a certain order of colors unless you set the color
# ## by plotting two different matplotlib typles to the same plot, both color indexes start at 0, i.e. blue
# ## so let's change the color, and marker type 

# plt.figure(3)
# plt.plot(x_data,y_data,marker = 'x',lw = 0, color = 'r')
# plt.scatter(x_data,y_data_2, color = 'g')

# ##There are many ways to customize a plot and you can always search the internet for quick tips
# ##stack overflow will likely be the most helpful, but there are plenty of options!
# ##We'll cover a few below that are most pertinent to science plotting 

# ##Adding a legend takes two steps, 1) label the data 2) add legend 
# ## To add a label to the data, add as an option inline of the plt.plot()
# ## Labels added as a string
# plt.figure(4)
# plt.plot(x_data,y_data, label = 'Sine Wave')

# ## To add a legend, to the *plot* 
# ## when editing the plot itself, a new plt function is called
# plt.legend() 

# #label axes (a change to the plot itself)
# plt.xlabel('x-axis (a.u.)')
# plt.ylabel('y-axis (a.u.)')
# plt.title('Great Data')

# #To change the limits of the x and y axis
# #note plt.xlim arguments = (left, right); plt.ylim(bottom,top)
# #plt.xlim(0) would set left minimum to 0 and allow the max to float
# plt.xlim(0,20)
# plt.ylim(-2,2)


###Now your turn###
#1. Make a plot with 20 data points from 0 to 100 following the equation:
    #  y = 2x + 15
    # with pink upward facing arrows and no connecting line
    # set the marker size to 15
    # set the marker edge color to grey
    # set the x-axis limits from the min to max of the x data
    # set the y-axis minimum limit to 0 and let max float
#2. On the same plot, with  250 points from 0 to 100
    # y = 20*sin(x) + 2x + 15
    # with green open circles and no connecting line 
#3. Format the plot
    # Label x-axis as "Practice Time"
    # Label y-axis as "Skill"
    # Label dataset 1 as "Theory"
    # Label dataset 2 as "In-Practice" 
    # Put a legend in the lower right corner 
    # Make x and y axis fontsize = 14 and bold
#4 Bonus
    # Change the axis tick labels to fontsize = 12
    # Add some text and an arrow pointing to a specific data point
x_data = np.linspace(0,100,20)
A = (2*x_data) + 15
plt.figure(100)
plt.plot(x_data,A, marker='^',color ='pink',lw=0,markersize = 15,markeredgecolor = 'grey', label = 'Theory')
x_data = np.linspace(0,100,250)
y_data = np.sin(x_data)
A = (2*x_data) + 15
plt.plot(x_data,A+(20*y_data),marker = 'o', color = 'g', markerfacecolor = 'none',lw = 0,label = 'In-Practice')
plt.ylim(0)
plt.xlim(0,100)
plt.legend(loc = 'lower right')
plt.xlabel("Practice Time",fontsize = 14, weight='bold')
plt.ylabel("Skill",fontsize = 14, weight = 'bold')
plt.xticks(size = 12)
plt.yticks(size = 12)
plt.annotate("My Favorite Point", xy=(40, 110), xytext=(10,160), arrowprops=dict(arrowstyle="->"))

file = r'E:\SETO9528 Data\FS\202204\PL\ssPL\202204-FS-1-f_ss-PL-f-1.txt'
data = np.genfromtxt(file, delimiter=)

