from setuptools import setup, find_packages
NAME = "fast_IO"
DESCRIPTION = "fast IO for pypy3 and python3"
LONG_DESCRIPTION = "This is a package for fast standard input and output for pypy3 and python3"

setup(
    name=NAME,
    version="0.0.1",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    py_modules=["fast_IO"],
    packages=find_packages()
)
