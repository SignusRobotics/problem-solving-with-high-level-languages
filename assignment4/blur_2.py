#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import cv2
import numpy as np

#import matplotlib
#import matplotlib.pyplot as plt 

filename = 'beatles.jpg'

image = cv2.imread(filename)
#image = cv2 . cvtColor ( image , cv2 . COLOR_BGR2RGB )

#cv2.imshow('I',image)
#cv2.waitKey()

# pad image: 
m, n, c = image.shape 

pad_image = np.zeros((m+2, n+2, c)) 

print(image.shape)


#plt.figure()
#plt.imshow(image, cmap='gray')
    
pimage = np.pad(image, (1,1), 'edge')
pad_image = pimage[:,:,1:4] 

# blurred image 

def blur_numpy(pad_image): 
    # define new image 
    image_blur2 = np.zeros((m,n,c))

    kernel_weight = 1/9 
    print(m,n)

    pad_image = pad_image.astype('uint32')
    #print(pad_image.shape)

    a = np.zeros((3*3,3)) 
    b = np.zeros((m,n,c, 9))

    start_time = time.process_time()

    for i in range(1,m+1): 
        for j in range(1,n+1):
            b[i-1,j-1,:, :] = pad_image[i-1:i+2, j-1:j+2, :].reshape(3,-1)


    image_blur2 = np.sum(b.reshape(-1,9), axis = 1).reshape(m,n,c) * kernel_weight

    end_time = time.process_time() 

    time_vec_numpy = end_time - start_time

    print("time used", time_vec_numpy)

    cv2.imwrite("beatles_blurred_numpy.jpg", image_blur2.astype('uint8'))

    return time_vec_numpy, image_blur2

#blur_numpy(pad_image)