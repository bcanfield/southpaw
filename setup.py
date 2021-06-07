from setuptools import setup, find_packages

VERSION = '0.0.7'
DESCRIPTION = 'MMA DFS Toolkit'
LONG_DESCRIPTION = 'MMA DFS Toolkit written in Python'

# Setting up
setup(
    name="southpaw",
    version=VERSION,
    author="Brandin Canfield",
    author_email="<brandincanfield@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['mma', 'dfs', 'lineup', 'optimizer', 'generator'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)
