import os
from setuptools import setup

setup(
    name = "viper",
    version = "5.0",
    author = "Siddharth Kannan",
    author_email = "kannan.siddharth12@gmail.com",
    description = "Password manager, written in Python and GUI generated using Tkinter.",
    license = "WTFPL",
    url = "http://siddharthkannan.webs.com",
    packages=['viper'],
    entry_points = {
        'gui_scripts' : ['viper = viper.viper5:main']
    },
    
    data_files = [
        ('share/applications/', ['viper.desktop'])
        
    ],    
    
    classifiers=[
        "License :: WTFPL",
    ],
)


#run the following command in the directory that has the file
#setup.py:

#python setup.py --command-packages=stdeb.command bdist_deb
