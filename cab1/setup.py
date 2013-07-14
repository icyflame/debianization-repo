import os
from setuptools import setup

setup(
    name = "cowsandbulls",
    version = "1.0",
    author = "Siddharth Kannan",
    author_email = "kannan.siddharth12@gmail.com",
    description = "A number guessing game.",
    license = "WTFPL",
    url = "http://siddharthkannan.webs.com",
    packages=['cab1'],
    entry_points = {
        'gui_scripts' : ['cowsandbulls = cab1.cab1:main']
    },
    
    data_files = [
        ('share/applications/', ['cab.desktop'])
        
    ],    
    
    classifiers=[
        "License :: WTFPL",
    ],
)


#run the following command in the directory that has the file
#setup.py:

#python setup.py --command-packages=stdeb.command bdist_deb
