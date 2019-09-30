#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import cv2
import numpy as np

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


def blur_python(pad_image,image): 
    """Blur an image with only python and pixelwise. 
    
    Args: 
        image (array, int): 3D array, image with dimensions m,n,c (height, width and channels). 
        pad_image (array, int) 3D array, padded height and width, with dimensions m+2, n+2, c. 

    Returns: 
        image_blur: blurred image, same dimensions as image.  
    """
    # define new image 
    m,n,c = image.shape
    image_blur = np.zeros((m,n,c))

    kernel_weight = 1/9 

    pad_image = pad_image.astype('uint32')

    for channel in range(0,c): 
        for i in range(1,m+1): 
            for j in range(1,n+1): 
                image_blur[i-1,j-1,channel] = kernel_weight * (pad_image[i-1, j-1, channel] + pad_image[i-1, j, channel] + pad_image[i-1,j+1, channel]
                + pad_image[i,j-1,channel] + pad_image[i, j, channel] + pad_image[i,j+1,channel] 
                + pad_image[i+1, j-1, channel] + pad_image[i+1, j, channel] + pad_image[i+1, j+1, channel])

    return image_blur #, time_elementwise 

if __name__ == '__main__': 
    pad_image, image = padImage()
    image_blur = blur_python(pad_image, image)
    cv2.imwrite("beatles_blurred_python.jpg", image_blur.astype('uint8'))
