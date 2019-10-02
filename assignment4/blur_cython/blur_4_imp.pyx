#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import cv2
import numpy as np
# cython: infer_types=True
cimport numpy as np
np.import_array()
#DTYPE = np.int

cpdef padImage():
    """Preprocess image before blurring.    

    Returns: 
        pad_image: padded image with dimensions: m+2, n+2, c
        image: original image with dimensions m,n,c.   
    """
    # Read image
    filename = 'beatles.jpg'

    cdef np.ndarray[np.uint_t, ndim = 3] image
    image = cv2.imread(filename).astype('uint')

    # cv2.imshow('I',image)
    # cv2.waitKey()

    # pad image:
    cdef int m, n, c
    #m, n, c = image.shape
    m = image.shape[0]
    n = image.shape[1]
    c = image.shape[2]

    cdef np.ndarray[np.uint_t, ndim = 3] pad_im
    pad_im = np.zeros((m+2, n+2, c), dtype=np.uint)

    cdef np.ndarray[np.uint_t, ndim = 3] pimage
    pimage = np.pad(image, (1, 1), 'edge')
    pad_im = pimage[:, :, 1:4]
    cdef np.ndarray[np.uint32_t, ndim = 3] pad_image
    pad_image = pad_im.astype('uint32')
    return pad_image, image


cpdef blur_python(np.ndarray[np.uint32_t, ndim=3] pad_image, np.ndarray[np.uint_t, ndim=3] image):
    """Blur an image with only python and pixelwise. 

    Args: 
        image (array, int): 3D array, image with dimensions m,n,c (height, width and channels). 
        pad_image (array, int) 3D array, padded height and width, with dimensions m+2, n+2, c. 

    Returns: 
        image_blur: blurred image, same dimensions as image.  
    """

    m = image.shape[0]
    n = image.shape[1]
    c = image.shape[2]

    cdef np.ndarray[np.double_t, ndim = 3] image_blur
    image_blur = np.zeros((m, n, c), dtype=np.double)

    cdef double kernel_weight
    kernel_weight = 1/9

    cdef int i, j, channel
    cdef int test

    for channel in range(0, c):
        for i in range(1, m+1):
            for j in range(1, n+1):
                test = ((pad_image[i-1, j-1, channel] + pad_image[i-1, j, channel] + pad_image[i-1, j+1, channel]
                         + pad_image[i, j-1, channel] + pad_image[i,
                                                                  j, channel] + pad_image[i, j+1, channel]
                         + pad_image[i+1, j-1, channel] + pad_image[i+1, j, channel] + pad_image[i+1, j+1, channel]))

                #test = test * kernel_weight
                test = test / 9

                image_blur[i-1, j-1, channel] = (test)

    # kernel_weight.astype('uint32')
    # cdef np.ndarray[np.uint8_t, ndim=3] im_blur
    #im_blur = image_blur.astype('uint8')
    # cv2.imwrite("beatles_blurred_python.jpg", image_blur)  # .astype('uint8'))
    #cv2.imwrite("beatles_blurred_python.jpg", im_blur)

    return image_blur

# if __name__ == '__main__':
#    blur_python()
    #pad_image, image = padImage()
    #image_blur = blur_python(pad_image, image)
    #cv2.imwrite("beatles_blurred_python.jpg", image_blur.astype('uint8'))


if __name__ == '__main__':
    # blur_python()
    pad_image, image = padImage()
    image_blur = blur_python(pad_image, image)
    cv2.imwrite("beatles_blurred_cython.jpg")  # , image_blur.astype('uint8'))
