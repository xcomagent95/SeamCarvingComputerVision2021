# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 18:55:38 2022

@author: Alexander Pilz
"""
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('computer_vision_lib.pyx'))
