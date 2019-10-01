#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import argparse

import cv2
import numpy as np

import blur_1  # python
import blur_2  # NumPy
import blur_3  # Numba


# class Blur():
parser = argparse.ArgumentParser(
    description='blur an image. Choose between 3 methods: python implementation (py), NumPy (numpy) or python with Numba (numba)')
parser.add_argument('--input', type=str,
                    default='beatles.jpg', help='input image, filename: ')
parser.add_argument(
    '--output', type=str, default='beatles_blur.jpg', help='blurred image, filename: ')
parser.add_argument('--method', type=str, default='py',
                    help='blur method', choices=['py', 'numpy', 'numba'])

args = parser.parse_args()

filename = args.input  # 'beatles.jpg'
out = args.output
blur_method = args.method
image = cv2.imread(filename)

# pad image:
m, n, c = image.shape
pad_image = np.zeros((m+2, n+2, c))
pimage = np.pad(image, (1, 1), 'edge')
pad_image = pimage[:, :, 1:4]

if blur_method == 'py':
    #_, time_elementwise = blur_1.blur_python(pad_image)
    blur_image = blur_1.blur_python(pad_image, image)
    #print("time used: ", time_elementwise)
elif blur_method == 'numpy':
    #_, time_elementwise = blur_2.blur_numpy(pad_image)
    blur_image = blur_2.blur_numpy(pad_image, image)

    #print("time used: ", time_elementwise)
elif blur_method == 'numba':
    #_, time_elementwise = blur_3.blur_numba(pad_image)
    blur_image = blur_3.blur_numba(pad_image, image)

    #print("time used: ", time_elementwise)
else:
    print("Not supported function")

cv2.imwrite(out, blur_image.astype('uint8'))

def blur_image(input_filename, output_filename = None): 
    image = cv2.imread(input_filename) 
    # pad image:
    m, n, c = image.shape
    pad_image = np.zeros((m+2, n+2, c))
    pimage = np.pad(image, (1, 1), 'edge')
    pad_image = pimage[:, :, 1:4]    

    #blur:
    kernel_weight = 1/9 

    m, n, c = image.shape 
    pad_image = pad_image.astype('uint32')

    blur_image = blur_2.blur_numpy(pad_image, image)
    if output_filename != None: 
        cv2.imwrite(output_filename, blur_image.astype('uint8'))
    #else: 
    #    cv2.imwrite("blur_image.jpg", blur_image.astype('uint8'))
    return blur_image


#if __name__ = '__main__':