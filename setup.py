from setuptools import setup
from Cython.Build import cythonize

setup(
    name='LiteraPy',
    ext_modules=cythonize("litera.py"),
    zip_safe=False,
)