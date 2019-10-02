#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random

# import assignment4.blur_1
import assignment4.blur_assignment4.blur_1 as blur1
import assignment4.blur_assignment4.blur_2 as blur2
import assignment4.blur_assignment4.blur_3 as blur3


class Test_blur:
    """Test modules in package blur_assignment4

    """

    def test_max_value_decreased_after_blurring_1(self):
        """Test 1.1 with python, max_value_decreased_after_blurring"""
        m, n, c = 400, 600, 3
        np.random.seed(42)

        image = np.random.randint(256, size=(m, n, c))
        pimage = np.pad(image, (1, 1), 'edge')
        pad_image = pimage[:, :, 1:4]
        image_blur = blur1.blur_python(pad_image, image)

        a = np.amax(image)
        b = np.amax(image_blur)

        assert a > b

    def test_max_value_decreased_after_blurring_2(self):
        """Test 1.2 with numpy, max_value_decreased_after_blurring"""
        m, n, c = 400, 600, 3
        np.random.seed(42)

        image = np.random.randint(256, size=(m, n, c))
        pimage = np.pad(image, (1, 1), 'edge')
        pad_image = pimage[:, :, 1:4]
        image_blur = blur2.blur_numpy(pad_image, image)

        a = np.amax(image)
        b = np.amax(image_blur)

        assert a > b

    def test_max_value_decreased_after_blurring_3(self):
        """Test 1.3 with numba, max_value_decreased_after_blurring"""
        m, n, c = 400, 600, 3
        np.random.seed(42)

        image = np.random.randint(256, size=(m, n, c))
        pimage = np.pad(image, (1, 1), 'edge')
        pad_image = pimage[:, :, 1:4]
        image_blur = blur3.blur_numba(pad_image, image)

        a = np.amax(image)
        b = np.amax(image_blur)

        assert a > b

    def test_image_blur_pixel_and_image_1(self):
        """Test 2.1 with python, blurred pixel == average pixel from image"""
        np.random.seed(42)
        m, n, c = 400, 600, 3
        image = np.random.randint(256, size=(m, n, c))
        pimage = np.pad(image, (1, 1), 'edge')
        pad_image = pimage[:, :, 1:4]
        image_blur = blur1.blur_python(pad_image, image)

        # Coordinates:
        m_t = np.random.randint(low=1, high=253, size=1)
        n_t = np.random.randint(low=1, high=253, size=1)
        c_t = np.random.randint(3, size=1)

        n_random = n_t[0]
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

        c_3 = image_blur[m_random, n_random, c_random]

        np.testing.assert_almost_equal(c_3, image_value_avg, 3)

    def test_image_blur_pixel_and_image_2(self):
        """Test 2.2 with numpy, blurred pixel == average pixel from image"""
        np.random.seed(78)
        m, n, c = 400, 600, 3
        image = np.random.randint(256, size=(m, n, c))
        pimage = np.pad(image, (1, 1), 'edge')
        pad_image = pimage[:, :, 1:4]
        image_blur = blur2.blur_numpy(pad_image, image)

        # Coordinates:
        m_t = np.random.randint(low=1, high=253, size=1)
        n_t = np.random.randint(low=1, high=253, size=1)
        c_t = np.random.randint(3, size=1)

        n_random = n_t[0]
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

        c_3 = image_blur[m_random, n_random, c_random]

        np.testing.assert_almost_equal(c_3, image_value_avg, 3)

    def test_image_blur_pixel_and_image_3(self):
        """Test 2.3 with numba, blurred pixel == average pixel from image"""
        np.random.seed(42)
        m, n, c = 400, 600, 3
        image = np.random.randint(256, size=(m, n, c))
        pimage = np.pad(image, (1, 1), 'edge')
        pad_image = pimage[:, :, 1:4]
        image_blur = blur3.blur_numba(pad_image, image)

        # Coordinates not on edges:
        m_t = np.random.randint(low=1, high=253, size=1)
        n_t = np.random.randint(low=1, high=253, size=1)
        c_t = np.random.randint(3, size=1)

        n_random = n_t[0]
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

        c_3 = image_blur[m_random, n_random, c_random]

        np.testing.assert_almost_equal(c_3, image_value_avg, 3)

    def test_add(self):
        m, n, c = 400, 600, 3
        assert m+n+c == 1003

    def test_image(self):
        m, n, c = 400, 600, 3

        image = np.random.randint(255, size=(m, n, c))
        image2 = np.random.randint(255, size=(m, n, c))
        # assert 1 != 2
        assert image[0, 0, 0] != image2[0, 0, 0]

    def test_random(self):
        np.random.seed(42)
        c = np.random.randint(255, size=1)
        b = np.random.randint(255, size=1)

        assert 102 == c[0]
        assert 179 == b[0]
