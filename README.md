# w3j


Installation:  `python setup.py install`

This will install the `w3j` package.  To access the SLATEC function
`drc3jm`, just do `from w3j import drc3jm`.  Example usage is as follows:

    >>> from w3j import drc3jm
    >>> import numpy as np
    >>> result = np.empty(5, dtype=float)
    >>> drc3jm(2,2,2,0,-2,2, result, 0)
    >>> result
    	array([ 0.23904572,  0.11952286, -0.23904572,  0.11952286,  0.23904572])