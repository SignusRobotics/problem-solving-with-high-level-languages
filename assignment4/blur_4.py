#!/usr/bin/env python
# -*- coding: utf-8 -*-

import blur_4_imp 
import cv2
import numpy as np

pad_image, image = blur_4_imp.padImage() 
image_blur = blur_4_imp.blur_python(pad_image,image)

cv2.imwrite("beatles_blurred_cython.jpg", image_blur.astype('uint8'))
