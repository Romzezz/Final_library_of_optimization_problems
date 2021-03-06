#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="Final_library_of_optimization_problems",
    version="0.0.2",
    author="Daniil Belotserkovskiy",
    description="A package with optimization functions",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Romzezz/Final_library_of_optimization_problems/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)

