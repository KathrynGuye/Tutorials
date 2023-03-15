# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:32:28 2022

@author: kguye
"""

import numpy as np
import os
import matplotlib.pyplot as plt
import h5py

data_file = r'G:\My Drive\FS SETO9528\SETO9528 Shared Folders\Raw Data Sharing\SETO Hyperspectral Files\h5 files\202208-FS-1-f_midcenter-second piece-532nm_rec.h5'
save_folder = data_file
obj = 20 ##objective magnification 

save = False

##loading h5 file##
hf = h5py.File(data_file, 'r') #loads h5 file
images=np.array(hf['Cube']['Images'])#your 3D data cube of pixel intensities; shape: [z,h,w], where z is # of slices
images=np.transpose(images) #transposes images; shape: [w,h,z] (optional, but then later arguments need to be adjusted)
wavelengths=np.array(hf['Cube']['Wavelength']) #an array of the wavelengths used (indexes match images index)
exposure_time = np.array(hf['Cube']['TimeExposure'])[0] #extracts the exposure time used (optional)

# ##cropping images##
# cropped_images = images[min_width:max_width, min_length:max_length,:] #(final ":" says for all wavelength slices)
# #for whole image: cropped_images = images[:,:,:]
cropped_images = images[:1024,:1024]/exposure_time
images = cropped_images 

##Determining pixel size from objective magnification
px = 6.45/obj
#Determining wavelength stepsize (assumes linear throughout cube)
stepsize = wavelengths[1]-wavelengths[0]

##Looking at single wavelength slice##
wavelength_slice = 750
wavelength_index = np.where(wavelengths == wavelength_slice)[0][0]
plt.figure()
plt.imshow(images[:,:,wavelength_index],extent=[0,px*images.shape[1],0,px*images.shape[0]],cmap = 'viridis') #extent converts pixels to um length
 #optional formatting below
plt.xlabel(r"x ($\mu$m)")
plt.ylabel(r"y ($\mu$m)")
cbar = plt.colorbar()
cbar.set_label("Intensity",rotation=270,fontsize=12, labelpad = 13) #formating colorbar 
min_intensity = images[:,:,wavelength_index].min() #identifying min intensity
max_intensity = images[:,:,wavelength_index].max() #identifying max intensity
# plt.clim(min_intensity,max_intensity) #or normalize to whatever intensities you want 

#plotting random pixel 
plt.figure()
plt.plot(wavelengths,images[100,100,:])
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (counts/s)')
plt.xlim(700,900)

#plotting average spectrum
average = np.sum(images[:,:,:],axis = 0)
average = np.sum(average[:,:],axis = 0)
plt.figure()
plt.plot(wavelengths,average)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (counts/s)')
plt.xlim(700,900)

# ##Statistics
# hist_array = np.ravel(images[:,:,wavelength_index])#converts 2d image aray to a 1d array containing all intensities 
# binsize = 50 #can set to whatever stepsize you want - should not be smaller than precision of instrument
# bins = np.arange(hist_array.min(),hist_array.max()+binsize,binsize)
# plt.figure()
# plt.hist(hist_array,bins=bins,facecolor = 'grey',edgecolor = 'black',lw=2)
# plt.xlabel("Intensity (counts)")
# plt.ylabel("Number of Pixels")

# if save == True:
#     plt.figure()
#     plt.savefig(save_folder+'/'+'filename.png',dpi=300,bbox_inches = "tight")