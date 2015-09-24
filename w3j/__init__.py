# -*- coding: utf-8 -*-

__version__ = "0.0"

try:
    __W3J_SETUP__
except NameError:
    __W3J_SETUP__ = False

if not __W3J_SETUP__:
    from ._w3j import drc3jm


        
