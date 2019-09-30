#!/usr/bin/python 
# -*- coding: utf-8 -*-

import time
import cv2
import numpy as np

filename = 'beatles.jpg'
image = cv2.imread(filename)

def face_detect(image):
    """Detect faces in image. Using the file haarcascade_frontalface_default.xml. 

    Args: 
        image array: 3D array with dimensions m,n,c. 
    
    Returns: 
        faces (list): list of coordinates of box where face recognized. x,y,height,width. 
    """
    m,n,c = image.shape
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(image, scaleFactor=1.025, minNeighbors=5, minSize=(30, 30))
    return faces 

def blur_faces(image, faces):
    """Blur part of image with coordinates from faces list.  

    Args: 
        image array: 3D array with dimensions m,n,c. 
        faces (list): list of coordinates of boxes in image where face recognized. x,y,height,width. 

    Returns: 
        blur_image: 3D array image with blurred parts where face is recognized. 
    """ 
    #for (x,y,h,w) in faces: 
    pimage = np.pad(image, (1,1), 'edge')
    pad_image = pimage[:,:,1:4] 

    m,n,c = image.shape

    #test = cv2.imread(filename)
    #image_blur = np.zeros(image.shape)
    image_blur = image

    kernel_weight = 1/9 
    #print(m,n)

    pad_image = pad_image.astype('uint32')
    #print(pad_image.shape)
    #print(image.shape)

    #start_time = time.clock()
    #start_time = time.process_time()

    for (y,x,h,w) in faces: 
        image_blur[x:x+h,y:y+w,0:c] = (pad_image[x:x+h,y:y+w,0:c]
                        + pad_image[x+1:x+h+1, y:y+w,0:c]
                        + pad_image[x+2:x+h+2, y:y+w,0:c]
                        + pad_image[x:x+h,     y+1:y+w+1,0:c]
                        + pad_image[x+1:x+h+1, y+1:y+w+1,0:c]
                        + pad_image[x+2:x+h+2, y+1:y+w+1,0:c]
                        + pad_image[x:x+h,     y+2:y+w+2,0:c]
                        + pad_image[x+1:x+h+1, y+2:y+w+2,0:c]
                        + pad_image[x+2:x+h+2, y+2:y+w+2,0:c])*kernel_weight
    
    #end_time = time.process_time() 

    #time_vec_numpy = end_time - start_time

    #print(end_time - start_time)
    return image_blur 

def anonymized():

    faces = face_detect(image) 

    temp_image = blur_faces(image,faces)
    #faces = face_detect(temp_image) 
    i=0
    #nr, coord = faces.shape
    nr, coord = faces.shape

    while nr > 0:
        i=i+1
        temp_image = blur_faces(temp_image,faces) 
        faces = face_detect(temp_image)
        #nr, coord = faces.shape

        nr = np.asarray(faces).size
        #nr = faces.size

        print(nr)

        
    print(i)
    cv2.imwrite("test2.jpg", temp_image.astype('uint8'))    

anonymized()


