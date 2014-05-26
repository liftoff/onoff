import os
import sys
import onoff
from setuptools import setup
from setuptools.command.install import install
from distutils.command.install import INSTALL_SCHEMES

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

extra = {}
major, minor = sys.version_info[:2] # Python version
if major == 2:
    from distutils.command.build_py import build_py
elif major == 3:
    PYTHON3 = True
    #from subprocess import getstatusoutput
    extra['use_2to3'] = True # Automatically convert to Python 3; love it!
    try:
        from distutils.command.build_py import build_py_2to3 as build_py
    except ImportError:
        print("Python 3.X support requires the 2to3 tool.")
        print(
            "It normally comes with Python 3.X but (apparenty) not on your "
            "distribution.\nPlease find out what package you need to get 2to3"
            "and install it.")
        sys.exit(1)

setup(
    name="onoff",
    cmdclass = {'build_py': build_py},
    version=onoff.__version__,
    description="A universal mixin to add on(), off(), and trigger() style event handling to any Python class.",
    author=onoff.__author__,
    author_email="daniel.mcdougall@liftoffsoftware.com",
    url="https://github.com/liftoff/onoff",
    license="Apache 2.0",
    py_modules=["onoff"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries",
        "Operating System :: OS Independent",
    ],
    **extra
)
