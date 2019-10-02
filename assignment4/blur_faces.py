#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import cv2
import numpy as np
import blur_assignment4.blur_2 as blur
#import blur_2 as blur


def face_detect(image):
    """Detect faces in image. Using the file haarcascade_frontalface_default.xml. 

    Args: 
        image array: 3D array with dimensions m,n,c. 

    Returns: 
        faces (list): list of coordinates of box where face recognized. x,y,height,width. 
    """
    #m, n, c = image.shape
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        image, scaleFactor=1.025, minNeighbors=5, minSize=(30, 30))
    return faces


def blur_faces(image, faces):
    """Blur part of image with coordinates from faces list.  

    Args: 
        image array: 3D array with dimensions m,n,c. 
        faces (list): list of coordinates of boxes in image where face recognized. x,y,height,width. 

    Returns: 
        blur_image: 3D array image with blurred parts where face is recognized. 
    """
    # for (x,y,h,w) in faces:
    pimage = np.pad(image, (1, 1), 'edge')
    pad_image = pimage[:, :, 1:4]

    m, n, c = image.shape
    for (x, y, h, w) in faces:
        image2 = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # define blurred image.
    image_blur = image2.copy()
    pad_image = pad_image.astype('uint32')

    for (y, x, h, w) in faces:
        image_blur[x:x+h, y:y+w, 0:c] = blur.blur_numpy(pad_image[x:x+h+2, y:y+w+2, 0:c],
                                                        image[x:x+h, y:y+w, 0:c])

    return image_blur


def anonymized():
    """Blur detected faces in image to not detectable. 

    """

    faces = face_detect(image)

    temp_image = blur_faces(image, faces)
    i = 0
    nr, _ = faces.shape

    while nr > 0:
        i = i+1
        temp_image = blur_faces(temp_image, faces)
        faces = face_detect(temp_image)
        nr = np.asarray(faces).size
        print(nr)

    print(i)
    cv2.imwrite('anonymized_blur.jpg', temp_image.astype('uint8'))


if __name__ == '__main__':
    filename = 'beatles.jpg'
    image = cv2.imread(filename)
    anonymized()
