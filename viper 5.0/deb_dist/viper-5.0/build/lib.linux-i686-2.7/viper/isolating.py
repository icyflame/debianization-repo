##File number 2
##
##This file has the function that can take a line from the file which is
##passed to it as parameter and return the four fields that are there in it
##as separate variables.
##
##This is a part of the program in Python Tkinter
##
##created on 9th April, 2013
##
##Modified 20th May, 2013
##
##    changes:
##
##        during the creation of VIPER 5, in the phase where we had to
##        show details in different windows. Lots of debugging code needed to be added.
##        in the main file and here too. That was added and removed.


from newRec import *

import string

def isolate(i):

    i = str(i)

    i = i.strip('\n')

    this = 'username:'
    other = 'account:'

    ##username

    un = i[string.find(i,this) + len(this):string.find(i,other)]
    this = other
    other = 'password:'

    ##account
    ac = i[string.find(i,this) + len(this):string.find(i,other)]
    this = other
    other = 'remarks:'

    ##password
    pas = i[string.find(i,this) + len(this):string.find(i,other)]
    this = other
    ##other = '\n'

    ##remarks

    i.strip()
    
    rem = i[string.find(i,this) + len(this):]

    rem = str(rem)   

    if not rem == '':

        if(rem[-1] == '\r' or rem[-1] == '\n'):

            rem = rem[:-1]

    ##print 'isolated record:',(un,ac,pas,rem)

    return (un,ac,pas,rem)

##script level testing code:

##app = record()
##
##app.getFromUser()
##
##un,ac,pas,rem = isolate(str(app))
##
##print un
##print ac
##print pas
##print rem
