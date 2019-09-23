#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import argparse 

import cv2
import numpy as np 

import blur_1 # python
import blur_2 # NumPy
import blur_3 # Numba 


parser = argparse.ArgumentParser(description='blur an image. Choose between 3 methods: python implementation (1), NumPy (2) or python with Numba (3)')
parser.add_argument('--input', type=str, default='beatles.jpg', help='input image, filename: ')
parser.add_argument('--output', type=str, default='beatles_blur.jpg', help='blurred image, filename: ')
parser.add_argument('--method', type=str, default='py', help='blur method', choices=['py', 'numpy', 'numba'])

args = parser.parse_args() 

filename = args.input # 'beatles.jpg' 
out = args.output 
blur_method = args.method 
image = cv2.imread(filename) 

#image = cv2 . cvtColor ( image , cv2 . COLOR_BGR2RGB )

#cv2.imshow('I',image)
#cv2.waitKey()

# pad image: 
m, n, c = image.shape 

pad_image = np.zeros((m+2, n+2, c)) 

print(image.shape)
    
pimage = np.pad(image, (1,1), 'edge')
pad_image = pimage[:,:,1:4] 

print(pad_image.shape)

if blur_method == 'py':
    _, time_elementwise = blur_1.blur_python(pad_image)
    print("time used: ", time_elementwise) 
