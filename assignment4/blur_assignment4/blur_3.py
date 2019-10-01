#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import cv2
import numpy as np 

import numba
from numba import jit 


def padImage():
    """Preprocess image before blurring.    
    
    Returns: 
        pad_image: padded image with dimensions: m+2, n+2, c
        image: original image with dimensions m,n,c.   
    """
    #Read image 
    filename = 'beatles.jpg'
    image = cv2.imread(filename)

    #cv2.imshow('I',image)
    #cv2.waitKey()

    # pad image: 
    m, n, c = image.shape 
    pad_image = np.zeros((m+2, n+2, c)) 
    pimage = np.pad(image, (1,1), 'edge')
    pad_image = pimage[:,:,1:4] 
    return pad_image, image 

@jit
#@jit(nopython=True)
def blur_numba(pad_image, image):
    """Blur an image with only python and pixelwise. Using numba jit.   
    
    Args: 
        image: 3D array, image with dimensions m,n,c (height, width and channels). 
        pad_image: 3D array, padded height and width, with dimensions m+2, n+2, c. 

    Returns: 
        image_blur: blurred image, same dimensions as image.  
    """
    # define new image 
    #image_blur = np.zeros((m,n,c))
    image_blur = np.zeros(image.shape)
    m, n, c = image.shape 

    kernel_weight = 1/9 
    #print(m,n)
    pad_image = pad_image.astype('uint32')

    #start_time = time.clock()
    #start_time = time.process_time()

    for channel in range(0,c): 
        for i in range(1,m+1): 
            for j in range(1,n+1): 
                image_blur[i-1,j-1,channel] = kernel_weight * (pad_image[i-1, j-1, channel] + pad_image[i-1, j, channel] + pad_image[i-1,j+1, channel]
                + pad_image[i,j-1,channel] + pad_image[i, j, channel] + pad_image[i,j+1,channel] 
                + pad_image[i+1, j-1, channel] + pad_image[i+1, j, channel] + pad_image[i+1, j+1, channel])

    #end_time = time.clock() 
    #end_time = time.process_time() 

    #time_elementwise = end_time - start_time 
    #print("time used", time_elementwise)


    #cv2.imwrite("beatles_blurred_numba.jpg", image_blur.astype('uint8'))

    #return time_elementwise, image_blur 
    return image_blur 

if __name__ == '__main__': 
    #blur_numba(pad_image)
    pad_image, image = padImage()
    image_blur = blur_numba(pad_image, image)
    cv2.imwrite("beatles_blurred_numba.jpg", image_blur.astype('uint8'))