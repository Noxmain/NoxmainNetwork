# by Noxmain
# -*- coding: utf-8 -*-
import setuptools

classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

setuptools.setup(
    name='NeuralNetwork',
    version='1.6.2',
    description="A package to create, train and test neural networks with mutible layers",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Noxmain/NeuralNetwork",
    author="Noxmain",
    author_email="noah.finalcut@gmail.com",
    license='MIT',
    classifiers=classifiers,
    packages=setuptools.find_packages()
)
