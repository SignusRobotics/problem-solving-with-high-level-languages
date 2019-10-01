#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random

#import assignment4.blur_1
import assignment4.blur_1
import assignment4.blur_2


# .blur_1 import blur_python
# import blur_assignment4 as assignment4  # .blur_1 import blur_python


# import blur_assignment4  # import blur_1
# from blur_1 import blur_python
# from blur_2 import *
# import blur
# from blur_1 import *
# import blur_1 as b


class Test_blur:

    def test_add(self):
        m, n, c = 400, 600, 3
        assert m+n+c == 1003

    def test_image(self):
        m, n, c = 400, 600, 3

        image = np.random.randint(255, size=(m, n, c))
        image2 = np.random.randint(255, size=(m, n, c))
        # assert 1 != 2
        assert image[0, 0, 0] != image2[0, 0, 0]
        # np.testing.assert_array_compare(image, image2)

    def test_max_value_decreased_after_blurring_1(self):
        """Test 1.1 max_value_decreased_after_blurring"""
        m, n, c = 400, 600, 3
        np.random.seed(42)

        image = np.random.randint(256, size=(m, n, c))
        pimage = np.pad(image, (1, 1), 'edge')
        pad_image = pimage[:, :, 1:4]
        # image_blur = np.zeros((m, n, c))
        # image_blur = blur_1.blur_python(pad_image, image)
        # image_blur = assignment4.blur_3.blur_numba(pad_image, image)
        image_blur = assignment4.blur_1.blur_python(pad_image, image)

        a = np.amax(image)
        # a = image.max()
        b = np.amax(image_blur)
        # b = image_blur.max()

        assert a > b

        # assert np.maximum(image) > np.maximum(image_blur)

    def test_random(self):
        np.random.seed(42)
        c = np.random.randint(255, size=1)
        b = np.random.randint(255, size=1)

        assert 102 == c[0]
        assert 179 == b[0]

    def test_image_blur_pixel_and_image(self):
        """Test 2.1 blurred pixel == average pixel from image"""
        np.random.seed(42)
        m, n, c = 400, 600, 3
        image = np.random.randint(256, size=(m, n, c))
        pimage = np.pad(image, (1, 1), 'edge')
        pad_image = pimage[:, :, 1:4]
        image_blur = assignment4.blur_1.blur_python(pad_image, image)

        # Coordinates:
        # m = np.random.randint(255, size=1)
        m_t = np.random.randint(low=1, high=253, size=1)
        n_t = np.random.randint(low=1, high=253, size=1)
        # c_random = np.random.randint(low=0, high=3, size=1)

        # n = np.random.randint(255, size=1)
        n_random = n_t[0]
        c_t = np.random.randint(3, size=1)
        c_random = c_t[0]

        m_random = m_t[0]

        image_value_avg = (pad_image[m_random, n_random, c_random]
                           + pad_image[m_random, n_random+1, c_random]
                           + pad_image[m_random, n_random+2, c_random]
                           + pad_image[m_random+1, n_random, c_random]
                           + pad_image[m_random+1, n_random+1, c_random]
                           + pad_image[m_random+1, n_random+2, c_random]
                           + pad_image[m_random+2, n_random, c_random]
                           + pad_image[m_random+2, n_random+1, c_random]
                           + pad_image[m_random+2, n_random+2, c_random])/9

        # image_value_avg = (pad_image[m_random-1, n_random-1, c_random]
        #                    + pad_image[m_random-1, n_random, c_random]
        #                    + pad_image[m_random-1, n_random+1, c_random]
        #                    + pad_image[m_random, n_random-1, c_random]
        #                    + pad_image[m_random, n_random, c_random]
        #                    + pad_image[m_random, n_random+1, c_random]
        #                    + pad_image[m_random+1, n_random-1, c_random]
        #                    + pad_image[m_random+1, n_random, c_random]
        #                    + pad_image[m_random+1, n_random+1, c_random])/9

        c_3 = image_blur[m_random, n_random, c_random]
        # print(c)
        # print(image_value_avg)

        np.testing.assert_almost_equal(c_3, image_value_avg, 1)
        # assert image_value_avg == c
        # assert 1 == 1
        # np.testing.assert_array_equal image_blur[m_random, n_random, c_random] == image_value_avg

    def test_image_blur_pixel_and_image_2(self):
        """Test 2.1 blurred pixel == average pixel from image"""
        np.random.seed(78)
        m, n, c = 400, 600, 3
        image = np.random.randint(256, size=(m, n, c))
        pimage = np.pad(image, (1, 1), 'edge')
        pad_image = pimage[:, :, 1:4]
        image_blur = assignment4.blur_2.blur_numpy(pad_image, image)

        # Coordinates:
        # m = np.random.randint(255, size=1)
        m_t = np.random.randint(low=1, high=253, size=1)
        n_t = np.random.randint(low=1, high=253, size=1)
        # c_random = np.random.randint(low=0, high=3, size=1)

        # n = np.random.randint(255, size=1)
        n_random = n_t[0]
        c_t = np.random.randint(3, size=1)
        c_random = c_t[0]

        m_random = m_t[0]

        image_value_avg = (pad_image[m_random, n_random, c_random]
                           + pad_image[m_random, n_random+1, c_random]
                           + pad_image[m_random, n_random+2, c_random]
                           + pad_image[m_random+1, n_random, c_random]
                           + pad_image[m_random+1, n_random+1, c_random]
                           + pad_image[m_random+1, n_random+2, c_random]
                           + pad_image[m_random+2, n_random, c_random]
                           + pad_image[m_random+2, n_random+1, c_random]
                           + pad_image[m_random+2, n_random+2, c_random])/9

        # image_value_avg = (pad_image[m_random-1, n_random-1, c_random]
        #                    + pad_image[m_random-1, n_random, c_random]
        #                    + pad_image[m_random-1, n_random+1, c_random]
        #                    + pad_image[m_random, n_random-1, c_random]
        #                    + pad_image[m_random, n_random, c_random]
        #                    + pad_image[m_random, n_random+1, c_random]
        #                    + pad_image[m_random+1, n_random-1, c_random]
        #                    + pad_image[m_random+1, n_random, c_random]
        #                    + pad_image[m_random+1, n_random+1, c_random])/9

        c_3 = image_blur[m_random, n_random, c_random]

        # print(c)
        # print(image_value_avg)

        np.testing.assert_almost_equal(c_3, image_value_avg, 1)
        # assert image_value_avg == c
        # assert 1 == 1
        # np.testing.assert_array_equal image_blur[m_random, n_random, c_random] == image_value_avg
