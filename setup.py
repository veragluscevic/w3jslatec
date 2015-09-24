#!/usr/bin/env python

import os
import sys
from numpy.distutils.core import setup, Extension
#from setuptools import setup, Extension
import numpy

# Hackishly inject a constant into builtins to enable importing of the
# package even if numpy isn't installed. Only do this if we're not
# running the tests!
if sys.version_info[0] < 3:
    import __builtin__ as builtins
else:
    import builtins
builtins.__W3J_SETUP__ = True
import w3j
version = w3j.__version__

# Publish the library to PyPI.
if "publish" in sys.argv[-1]:
    os.system("python setup.py sdist upload")
    sys.exit()

# Push a new tag to GitHub.
if "tag" in sys.argv:
    os.system("git tag -a {0} -m 'version {0}'".format(version))
    os.system("git push --tags")
    sys.exit()

# Set up the compiled extension.
src = [os.path.join('w3j','slatec_3j.f90')]
src_pyx = [os.path.join('w3j','_w3j.pyx')]
ext = [Extension('w3j._w3j',  sources=src)]
#       Extension('w3j._w3j_pyx', sources=src_pyx,
#                 include_dirs=numpy.get_include())]



setup(
    name="w3j",
    version=version,
    author="Timothy D. Morton",
    author_email="tim.morton@gmail.com",
    url="https://github.com/timothydmorton/w3j",
    license="MIT",
    packages=["w3j"],
    ext_modules=ext,
    description="Calculating Wigner 3j",
    long_description=open("README.md").read(),
    #package_data={"": ["README.rst", "LICENSE"]},
    #include_package_data=True,
    #cmdclass={'build_ext': build_ext},
    classifiers=[
        # "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
