#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import numpy as np 

from blur import * 

m,n,c = 400,600,3

def test_max_value_decreased_after_blurring_1(self):
    """Test 1.1 max_value_decreased_after_blurring"""
    
    m,n,c = 400,600,3

    image = np.random.randint(255, size=(m,n,c))
    pimage = np.pad(image, (1,1), 'edge')
    pad_image = pimage[:,:,1:4] 
    image_blur = blur_1.blur_python(pad_image, image)
    assert np.max(image) > np.max(image_blur)

def test_max_value_decreased_after_blurring_2(self):
    """Test 1.2 max_value_decreased_after_blurring"""
    
    m,n,c = 400,600,3

    image = np.random.randint(255, size=(m,n,c))
    pimage = np.pad(image, (1,1), 'edge')
    pad_image = pimage[:,:,1:4] 
    image_blur = blur_2.blur_numpy(pad_image, image)
    assert np.max(image) > np.max(image_blur) 

def test_max_value_decreased_after_blurring_3(self):
    """Test 1.3 max_value_decreased_after_blurring"""
    
    m,n,c = 400,600,3

    image = np.random.randint(255, size=(m,n,c))
    pimage = np.pad(image, (1,1), 'edge')
    pad_image = pimage[:,:,1:4] 
    image_blur = blur_3.blur_numba(pad_image, image)
    assert np.max(image) > np.max(image_blur) 

def test_image_blur_pixel_and_image(self): 
    """Test 2.1 blurred pixel == average pixel from image"""
    
    m,n,c = 400,600,3
    
    image = np.random.randint(255, size=(m,n,c))
    pimage = np.pad(image, (1,1), 'edge')
    pad_image = pimage[:,:,1:4] 
    image_blur = blur_1.blur_python(pad_image, image)

    # Coordinates: 
    m_random = np.random.randint(255, size=1)
    n_random = np.random.randint(255, size=1)
    c_random = np.random.randint(3, size=1)


    image_blur[i-1,j-1,channel] = kernel_weight * (pad_image[i-1, j-1, channel] + pad_image[i-1, j, channel] + pad_image[i-1,j+1, channel]
    + pad_image[i,j-1,channel] + pad_image[i, j, channel] + pad_image[i,j+1,channel] 
    + pad_image[i+1, j-1, channel] + pad_image[i+1, j, channel] + pad_image[i+1, j+1, channel])




    image_value_avg = pad_image[m_random-1,n_random-1,c_random]+ pad_image[m_random-1,n_random,c_random] + pad_image[m_random-1,n_random+1,c_random] 
                        + pad_image[m_random,n_random-1,c_random] + pad_image[m_random,n_random,c_random] + pad_image[m_random,n_random+1,c_random]
                        + pad_image[m_random+1,n_random-1,c_random] + pad_image[m_random+1,n_random,c_random] + pad_image[m_random+1,n_random+1,c_random]


    assert image_blur[[m_random,n_random,c_random] == image_value_avg 




