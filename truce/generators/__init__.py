from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'MMA DFS Toolkit'
LONG_DESCRIPTION = 'MMA DFS Toolkit written in Python'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="truce",
    version=VERSION,
    author="Brandin Canfield",
    author_email="<brandincanfield@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['mma', 'dfs', 'lineup', 'optimizer', 'generator'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)
