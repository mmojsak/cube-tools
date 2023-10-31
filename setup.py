# coding: utf-8
from setuptools import setup

setup(
    name="cube_tools",
    version="1.0",
    description="A python library and tool to read in and manipulate Gaussian cube files.",
    keywords="gaussian cube file manipulation",
    url="https://github.com/mmojsak/cube-tools",
    author="Mateusz Mojsak",
    author_email="",
    classifiers=[
        "Environment :: Console",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    py_modules=[
        "cube_tools",
    ],
    entry_points={
        "console_scripts": [
            "cube_tools = cube_tools:main",
        ],
    },
    install_requires=[
        "numpy>=1.12.0",
        "scipy>=0.19.1",
        "scikit-image>=0.14.1",
    ]
)
