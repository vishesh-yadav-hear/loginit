# setup.py

from setuptools import setup, find_packages

setup(
    name="loginit",
    version="0.1.0",
    packages=find_packages(),
    description="A simple library to greet users",
    author="Vishesh Yadav",
    author_email="visheshyadabhear@gmail.com",
    url="https://github.com/vishesh-yadav-hear/loginit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)