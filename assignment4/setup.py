
from distutils.core import setup 
from Cython.Build import cythonize 

setup(
    name = "Blur", 
    #ext_modules = cythonize("*.pyx"),
    ext_modules = cythonize("blur_4.pyx"),

    #ext_modules = cythonize("helloworld.pyx"),

)

# python setup.py build_ext --inplace 