#!/usr/bin/env python

import numpy as np
import numba
from numba import jit
import ctypes as ct
from numpy.ctypeslib import ndpointer

from w3j import drc3jm

"""
_w3j = np.ctypeslib.load_library('_w3j', '../build/lib.macosx-10.5-x86_64-2.7/w3j')

drc3jm = _w3j.drc3jm_
drc3jm.argtypes = [ct.c_int, ct.c_int, ct.c_int, 
                   ct.c_int, ct.c_int, ct.c_int,
                   ct.POINTER(ct.c_double),
                   ct.c_int]
drc3jm.restype = ct.c_void_p
"""
"""
from cffi import FFI
ffi = FFI()

lib = ffi.dlopen('../build/lib.macosx-10.5-x86_64-2.7/w3j/_w3j.so')
ffi.cdef('void drc3jm_(double, double, double, double, double, double, double*, int);')
drc3jm = lib.drc3jm_
"""

@jit#(nopython=True)
def w3j_ms(l1, l2, l3, m1):
    """
    for l1, l2, l3, m1

    returns w3js from m2 from -l2 to +l2
    """
    result = np.empty(2*l2 + 1, dtype=np.float64)
    ier = 0
    drc3jm(l1, l2, l3, m1, -l2, l2, result, ier)
    return result

print(w3j_ms(2,2,2,0))
