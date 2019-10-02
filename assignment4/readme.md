# README 
Assignment4 folder: 
### 4.1 blur image python implementation 

Defined in the script: 
#!/usr/bin/env python

run alone with: 

python3 blur_1.py 

Output example: 

Saves a blurred image of beatles if run as main. 

### 4.2 blur an image with vectorized numpy implementation. 

Same as 4.1 script name: blur_2.py 

Saves a blurred image of beatles if run as main. 

python3 blur_2.py 


### 4.3 Blur an image by using numba and same implementation as 4.1. 

Same as 4.1 script name: blur_3.py '

python3 blur_3.py 

Saves a blurred image of beatles if run as main. 


### 4.4 Cython implementation with python implementation 

subfolder blur_cython 

Scripts: 
    setup.py 
    blur_4_imp.pyx 
    blur_4.py 

python3 setup.py build_ext --inplace 
python3 blur_4.py 

### Timed functions. 

using jupyter notebook for estimate time for each relevant functions for python, numpy and numba. For cython using script and for loop. 

### 4.5 

Script: 
    blur.py 

Run: 
    Python3 blur.py --input = input_filename.jpg --output = output_filename.jpg --method = [python,numpy,numba] 


Three optional arguments:
    input (str) : name of an image in same folder. default: 'beatles.jpg'
    output (str) : Any choosen string with image ending png,jpg.  default: 'beatles_blur.jpg'
    method (str) : name of an image in same folder. default: 'python'
 

### 4.6 Package and testing. 

Scripts: 
setup.py 
__init__.py 

Implemented function blur_image in script blur.py. 


### test_blur.py  

All tests have been executed with pytest using the Python extension in Visual Studio Code on Windows 10. Was not able to install pytest in Ubuntu using WSL (Windows subsystem for Linux). ```.vscode/settings.json``` for pytest configuration.

### 4.7 blurring faces to not recognized by the facedetector 

Script: 
    blur_faces.py 
    haarcascade_frontalface_default.xml

Run: 
    python3 blur_faces.py 

Running as main: using example image, 'beatles.jpg'

Output: approximately 202 blurred iterations. 
