#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import cv2
import numpy as np
#import timeit  


#def blur_wrapper(): 
#    pad_image, image = padImage()
#    image_blur = blur_numpy(pad_image, image)

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

# blurred image 
### Without forloops 

# pad image: 
#pimage = np.pad(image, (1,1), 'edge')
#pad_image = pimage[:,:,1:4] 
#pad_image = pad_image.astype('uint32')


# blurred image 

def blur_numpy(pad_image, image): 
    """Blur an image with one vectorized operation, using numpyslicing.  
    
    Args: 
        image: 3D array, image with dimensions m,n,c (height, width and channels). 
        pad_image: 3D array, padded height and width, with dimensions m+2, n+2, c. 

    Returns: 
        image_blur: blurred image, same dimensions as image.  
    """
    
    
    # define new image 
    image_blur = np.zeros(image.shape)
        
    #pad_image = np.pad(image, ((1,1), (1,1), (0,0)))
    #pad_image = np.pad(image, ((1,1), (1,1), (0,0)), 'edge')

    kernel_weight = 1/9 

    m, n, c = image.shape 
    pad_image = pad_image.astype('uint32')


    #blur image without forloops. 
    image_blur[0:m,0:n,0:c] = ( pad_image[0:m, 0:n, 0:c]
                + pad_image[1:m+1, 0:n, 0:c]
                + pad_image[2:m+2, 0:n, 0:c]
                + pad_image[0:m, 1:n+1, 0:c]
                + pad_image[1:m+1, 1:n+1, 0:c]
                + pad_image[2:m+2, 1:n+1, 0:c]
                + pad_image[0:m, 2:n+2, 0:c]
                + pad_image[1:m+1, 2:n+2, 0:c]
                + pad_image[2:m+2, 2:n+2, 0:c]) 

    image_blur *= kernel_weight

    return image_blur 

#def time_test(pad_image, image): 
#    timeit blur_numpy(pad_image, image)

if __name__ == "__main__":
    #import timeit 
    #blur_wrapper() 
    pad_image, image = padImage()
    image_blur = blur_numpy(pad_image, image)
    cv2.imwrite("beatles_blurred_numpy.jpg", image_blur.astype('uint8'))
    
    #print(timeit.timeit("blur_wrapper()",setup="from __main__ import blur_wrapper"), number=1)

    #print(timeit.timeit("blur_numpy(pad_image, image)",setup="from __main__ import blur_numpy"))


    #time_test(pad_image, image)
