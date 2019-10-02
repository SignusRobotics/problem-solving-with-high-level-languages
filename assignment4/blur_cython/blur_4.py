#!/usr/bin/env python
# -*- coding: utf-8 -*-

import blur_4_imp
import cv2
import numpy as np
import time


def test():
    pad_image, image = blur_4_imp.padImage()
    image_blur = blur_4_imp.blur_python(pad_image, image)
    return image_blur


if __name__ == "__main__":
    #import timeit
    pad_image, image = blur_4_imp.padImage()

    current_time = 0
    n = 100  # 10000
    start_time = time.time()
    for i in range(0, n):
        image_blur = blur_4_imp.blur_python(pad_image, image)

        # if i % 100 == 0:
        # print(i)

    end_time = time.time()

    time_used = end_time - start_time
    time_used_pr_loop = time_used/n

    print(time_used_pr_loop)

    # test()
    #print(timeit.timeit("test()", setup="from __main__ import test"), number=1)
    cv2.imwrite("beatles_blurred_cython.jpg", image_blur.astype('uint8'))
