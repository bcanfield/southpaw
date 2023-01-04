from setuptools import setup, find_packages

VERSION = '2.0.2'
DESCRIPTION = 'Python Fanduel API'
LONG_DESCRIPTION = 'Automate your DFS experience with this Python Fanduel API'

# Setting up
setup(
    name="southpaw",
    version=VERSION,
    author="Brandin Canfield",
    author_email="<brandincanfield@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['fanduel', 'api', 'mma', 'dfs',
              'lineup', 'optimizer', 'generator'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)
