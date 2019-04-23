#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:02:09 2019

@author: Simon
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#1
def heart(im):
    m=im.shape[0]  #height
    n=im.shape[1]   #width
    x,y=np.ogrid[0:m,0:n]

    a=1.2*m/n
    mask=(2*m/5+a*y<x)      #mask1: the lower left 
    mask2=(8*m/5-a*y<x)     #mask2: lower right
    #mask3: upper left
    mask3=(16.0/3.0*m/n/n*y*y-43.5/15.0*m/n*y+2.0*m/5.0>x)&(x<=2*m/5)&(y<=n/2)
    #mask4: upper right
    mask4=(16.0/3.0*m/n/n*y*y-37.7/5.0*m/n*y+8.0*m/3.0>x)&(y>=n/2)&(y<=n)

    #set all mask to pink
    im[mask] = [1,0,1]
    im[mask2]=[1,0,1]
    im[mask3]=[1,0,1]
    im[mask4]=[1,0,1]

    plt.imshow(im)
    plt.show()
    
    
#2
def blurring(im,method):
    im=np.array(im[:,:,0],dtype="float") 
    newIm=im.copy()
    #set up filter to be changed later
    filterx=np.array([[0]*5]*5,dtype="float")
    if method == "Gaussian":
        for i in range (5):
            for j in range (5):
        #use equation to change filter
                filterx[i,j]=np.exp(-((i-4*0.5)**2)+(j-4*0.5)**2)/(2.0)
        filter_sum=np.sum(filterx)
        filterx=filterx/filter_sum
    #if uniform, just assume k=5 and change the filter
    elif method == "uniform":
        filterx=0.04
    else :
        return "wrong input"
    #apply filter and get the value
    for i in range (2,im.shape[0]-2):
        for j in range (2,im.shape[1]-2):
            newIm[i,j]=np.sum(im[i-2:i+3,j-2:j+3]*filterx)
    newIm=np.repeat(newIm[:,:,np.newaxis],3,axis=2)
    plt.imshow(im)
    plt.show()

#3
def detect_edge(im,method):
    newIm=im.copy()
    #convert to greyscale just in case
    im=np.array(im[:,:,0],dtype="float") 
    #two filters
    vertical_filter=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    horizontal_filter=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    for i in range(1,im.shape[0]-1):
        for j in range (1,im.shape[1]-1):
            #for every pixel, get a score by applying the filter and sum up and normalize

            if method == "vertical":
                score=(np.sum(im[i-1:i+2,j-1:j+2]*vertical_filter)+4)/8
            elif method =="horizontal":
                score=(np.sum(im[i-1:i+2,j-1:j+2]*horizontal_filter)+4)/8
            elif method == "both":
                vscore=np.sum(im[i-1:i+2,j-1:j+2]*vertical_filter)
                hscore=np.sum(im[i-1:i+2,j-1:j+2]*horizontal_filter)
                score=(vscore**2+hscore**2)**0.5/4
            else: 
                return "wrong input"
            #apply color to each score
            if(score>0.5):
                newIm[i,j]=[1.0,1.0,1.0]
            elif(score<0.5):
                newIm[i,j]=[0.0,0.0,0.0]
            elif(score==0.5):
                newIm[i,j]=[0.5,0.5,0.5]    


    plt.imshow(newIm)
    plt.show()