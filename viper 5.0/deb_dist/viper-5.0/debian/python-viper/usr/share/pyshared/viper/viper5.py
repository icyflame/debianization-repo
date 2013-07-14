##VIPER 5.0
##
##CREATED BY SIDDHARTH KANNAN
##
##WRITTEN ON PYTHON 2.7 AND TKINTER 8.5
##
##OS:LINUX MINT 14 NADIA


##     This program is free software. It comes without any warranty, to
##     the extent permitted by applicable law. You can redistribute it
##     and/or modify it under the terms of the Do What The Fuck You Want
##     To Public License, Version 2, as published by Sam Hocevar. See
##     http://www.wtfpl.net/ for more details.


##Main File
##
##Main file for VIPER 4 GUI using Tkinter 8.5 and Written in Python 2.7
##
##Revision history for this file is as so:
##
##created 18th May, 2013
##
##
##    changes:
##
##        changed the function that will display the records without password.
##        and now the details are shown in different toplevel windows in case
##        there are more than 20 records.
##
##        have to find a way to do this even in the other functions
##
##Modified 19th May, 2013
##
##    changes:
##
##        the changes were made in the seeing function. Now I cant call the function
##        that I used to call everytime as now even the windows are different and
##        everything needs to be done at the same time. So what I did is that I copied
##        the code from the function to the seeing function. Need to do this for:
##
##            1. modification
##            2. deletion
##
##        although this makes the code longer and is very hard to debug at this
##        point i am not able to understand how to handle this situation better.
##
##        major bug has been found in the file that was used to transfer from
##        viper 3 to viper 4 GUI. the ':' colon after username is not being appended
##        inside the new file.
##
##Modified 20th May, 2013
##
##    changes:
##
##        final changes made to the multiple windows. A new button added at the bottom that says
##        "see next page" which will take the user to the next page.
##
##        copies of the file saved. and code cleaned up.
##
##            - all print statements were removed
##            - all the 'raw_input()' were removed
##
##        code cleaned up at 1526 hrs. The new module encryption created.
##        It was found that after the window has been closed the code reaches
##        the lines after mainloop.
##
##        thus decided that the decryption will happen at the beginning. Before the Tk() instance
##        started and the encryption and storage will happen at the end.
##
##        1534 hrs. All functions are running fine. Only encryption work
##        remaining.

        
from Tkinter import *

from newRec import *

from isolating import *

from modifying import *

from hashlib import *

import tkMessageBox

import tkSimpleDialog

import tkFont

import string

import os

import encryption

salt = 'developedbysiddharthkannan'

SHOW_TOPBAR = True  ##varibale will control whether the top bar with the three close, minimise, restore buttons
                    ##will be shown or not.

CHANGE_SIZE = True

def setDefault():

    '''sets the default masterkey to \'abcd\''''

    m = 'abcd'

    m = m + salt

    m = sha1(m)
    m = m.hexdigest()

    filin = open('mast','w')

    filin.write(m)

    filin.close()

#setDefault()

class VIPER(object):
    def __init__(self):

        '''class function that will initialise an object'''

        self.window = Tk()

        self.window.title('Visual Interface for Password Entry and Retreival')

        self.big = tkFont.Font(family='Helvetica',size=20)

        root = self.window

        # make it cover the entire screen
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.overrideredirect(not SHOW_TOPBAR)
        root.geometry("%dx%d+0+0" % (w, h))


        self.w = w
        self.h = h
        
        self.initBindings()

        self.initFiles()

        self.initFrameAndButtons()


    ################################

##      FUNCTIONS FOR INITIALISING

    ################################

    def initFiles(self):

        try:
            a = open(fileName,'r')

        except IOError:

            a = open(fileName,'w')


        a.close()

        try:
            a = open('mast','r')

        except IOError:

            setDefault()
            

    def initBindings(self):

        self.window.bind('<Escape>',self.quitwin)

    def initFrame(self):

        '''initialises the frame using the pack method

           ideal for all kinds of activities with buttons or labels'''

        try:
            self.frame.destroy()

            self.a.destroy()

        except:
            pass

        self.frame = Frame(self.window,width=600,height=500)
        self.frame.pack()
        self.frame.pack_propagate(not CHANGE_SIZE)

    def initFrameAndButtons(self):

        '''this function will initialise the frame and also the buttons
            that are a part of VIPER's main menu'''

        self.initFrame()

        self.initButtons()

    def initFrameForTableDisplay(self):


        '''initialises the frame using the grid method.
            this is ideal to create things like tables and other
            ways that may be used to present tabular data to the user'''

        try:
            self.frame.destroy()

        except:
            pass

        self.frame = Frame(self.window,width=500,height=500)
        self.frame.grid()

##        if self.getnumrec() > 10:
##
##            self.frame.grid_propagate(1)
##
##        else:
##
##            self.frame.grid_propagate(1)


            

    def initButtons(self):

        '''function that will initialise all the buttons into the main frame.
            must be called only after any one of the frame initialising
            functions are called'''

        ##Button for new record

        listOfButtons = []

        listOfButtons.append(Button(self.frame,text='Enter a new record',command=self.getNewRec))
        listOfButtons.append(Button(self.frame,text='See all the stored records',command=self.seeAllRecordsWithoutPassword))
        listOfButtons.append(Button(self.frame,text='See the password of an account',command=self.showTableForSeeing))
        listOfButtons.append(Button(self.frame,text='Modify an account',command=self.modify))
        listOfButtons.append(Button(self.frame,text='Delete an account',command=self.delAcc))
        listOfButtons.append(Button(self.frame,text='See the number of records stored in file',command=self.showNumRec))
        listOfButtons.append(Button(self.frame,text='Change the master key',command=self.changeMastKey))
        listOfButtons.append(Button(self.frame,text='Delete all records',fg='white',bg='red',command=self.confirmDelete))
        listOfButtons.append(Button(self.frame,text='QUIT',fg='red',bg='black',command=self.quitwin))


        for i in range(len(listOfButtons)):

            listOfButtons[i].config(font=self.big)

            listOfButtons[i].pack(side='top')


    ###################################

##      GENERAL FUNCTIONS

    ###################################


    def reinitialise(self):

        '''this will delete the existing frame and initialise a new frame
            along with all the buttons as they were on the main menu'''

        try:

            self.frame.destroy()

            for i in self.Lwindows:

                i.destroy()

        except:

            pass

        self.initFrameAndButtons()


    def show(self,record='',ev=None):

        '''this will show the user the details of the account that he has decided
            to view'''
        
        tkMessageBox.showinfo('Details of selected account',record)
                    

    def rearrangeFiles(self):

        '''will remove the basic file and rename the file temp as viper'''

        os.remove(fileName)

        os.rename('temp',fileName)

    def checkpoint(self):

        ##first take the masterKey from the file
        try:

            inFile = open('mast','r')

        except IOError:

            self.quitwin()

            tkMessageBox.showinfo('sorry','The master key file is not available.\
We are unable to proceed. Go to siddharthkannan.webs.com and download the default\
 master key file. Goodbye')

            import sys
            sys.exit()

        M = inFile.read()

        inFile.close()

        temp = tkSimpleDialog.askstring('master key','Enter your master key:',show='*')

        temp = temp + salt

        temp = sha1(temp)

        temp = temp.hexdigest()

        if not temp == M:

            self.unauthorised()

            tkMessageBox.showinfo('access denied','Unauthorised access has been \
detected. Sorry. We can\'t allow you to continue. Goodbye.')

            self.window.destroy()

            import sys
            sys.exit()

        else:

            return

    #############################

##          NEW RECORD

    #############################    


    def getNewRec(self):

        '''this function will take a new record from the user and check if
            all the fields are empty. if this is the case then the new record will
            not be written to the file and the user will be given a message
            reflecting this'''


        self.checkpoint()

        app = record()

        self.win = self.window

        self.win.withdraw()

        app.getFromUser()

        a = isolate(app)

        self.win.deiconify()

        isEmpty = True

        for i in a:
            if i != '':
                isEmpty = False

        if isEmpty:
            tkMessageBox.showinfo('Warning','The record you entered has all \
fields empty. We will not write it to the file')

            self.win.update()
            self.win.deiconify()

            return

        out = open(fileName,'a')

        out.write(str(app))

        out.close()

        tkMessageBox.showinfo('Success','The operation was successful. The new record\
 was written to file')


    ###########################################

##     SEE RECORDS WITHOUT PASSWORD(TABLE)

    ###########################################

    def seeAllRecordsWithoutPassword(self):

        '''this will initialise a table that will show all the accounts
            with only the usernames and the accounts'''

        self.getNumRec = self.getnumrec

        self.Lwindows = []

        inFile = open(fileName,'r')

        self.checkpoint()

        startRow = 0
        serialColumn = 1
        unColumn = 2
        acColumn = 3

        counter = startRow + 1

        copy = self.frame    ##storing the current windows frame location
                            ##in memory for further access later.

        for i in inFile:  ##i contains one full record with all the parameters in a record

            if (counter - 1) % 20 == 0:

                y = Toplevel()

                self.Lwindows.append(y)

                z = Frame(y)

                z.grid()

                Label(z,text='   Serial   ',width=7).grid(row=startRow,column=serialColumn)

                Label(z,text='   Username   ').grid(row=startRow,column=unColumn)
                
                Label(z,text='   Account   ').grid(row=startRow,column=acColumn)


            un,ac,pas,rem = isolate(i)

            a = isolate(i)            

            Label(z,text=str(counter-startRow),width=7).grid(row=counter,column=serialColumn)

            j = un
            Label(z,text=j).grid(row=counter,column=unColumn)


            j = ac
            Label(z,text=j).grid(row=counter,column=acColumn)

            counter += 1

        for i in self.Lwindows:

            ##check if it is the last window.
            ##if it is not then add a button that says "go te next page"
            
            if not i == self.Lwindows[-1]:
                Button(i,text='See next page',command=i.destroy).grid(row=21,column=2)

            Button(i,text='Back To Main Menu',command=self.reinitialise).grid(row=22,column=2)

        inFile.close()

        self.frame = copy

    #########################################

##      SEEING THE DETAILS OF ANY ACCOUNT

    ##########################################


    def showTableForSeeing(self):

        '''this function will give the user the option to see the complete
            details of any one of the records using a series of buttons'''

        self.getNumRec = self.getnumrec

        self.Lwindows = []

        inFile = open(fileName,'r')

        self.checkpoint()

        startRow = 0
        serialColumn = 1
        unColumn = 2
        acColumn = 3

        counter = startRow + 1

        copy = self.frame    ##storing the current windows frame location
                            ##in memory for further access later.

        for i in inFile:  ##i contains one full record with all the parameters in a record

            if (counter - 1) % 20 == 0:

                y = Toplevel()

                self.Lwindows.append(y)

                z = Frame(y)

                z.grid()

                Label(z,text='   Serial   ',width=7).grid(row=startRow,column=serialColumn)

                Label(z,text='   Username   ').grid(row=startRow,column=unColumn)
                
                Label(z,text='   Account   ').grid(row=startRow,column=acColumn)


            un,ac,pas,rem = isolate(i)

            a = isolate(i)            

            Label(z,text=str(counter-startRow),width=7).grid(row=counter,column=serialColumn)

            j = un
            Label(z,text=j).grid(row=counter,column=unColumn)


            j = ac
            Label(z,text=j).grid(row=counter,column=acColumn)

            thisrecord = 'Username:' + un + '\nAccount:' + ac + '\nPassword:'\
                         + pas + '\nRemarks:' + rem

            Button(z,text=(':See details'),\
                                   command=self.callbackForShow(thisrecord)).grid(row=counter,\
                                                                                  column=acColumn + 1)

            counter += 1

        for i in self.Lwindows:

            ##check if it is the last window.
            ##if it is not then add a button that says "go te next page"
            
            if not i == self.Lwindows[-1]:
                Button(i,text='See next page',command=i.destroy).grid(row=21,column=2)

            Button(i,text='Back To Main Menu',command=self.reinitialise).grid(row=22,column=2)

        inFile.close()

        self.frame = copy        

    def callbackForShow(self,thisrecord):
        
        """ returns a callback for self.show """
        def callback():                 # make a new function
            self.checkpoint()       # check if the user is authorised
            self.show(thisrecord)    # that shows the given record

            self.reinitialise()
        return callback                 # return this function


    #######################################

##      MODIFY AN ACCOUNT

    #######################################

    def modify(self):
        '''allows to modify any one field'''

        self.getNumRec = self.getnumrec

        self.Lwindows = []

        inFile = open(fileName,'r')

        self.checkpoint()

        startRow = 0
        serialColumn = 1
        unColumn = 2
        acColumn = 3

        counter = startRow + 1

        copy = self.frame    ##storing the current windows frame location
                            ##in memory for further access later.

        for i in inFile:  ##i contains one full record with all the parameters in a record

            if (counter - 1) % 20 == 0:

                y = Toplevel()

                self.Lwindows.append(y)

                z = Frame(y)

                z.grid()

                Label(z,text='   Serial   ',width=7).grid(row=startRow,column=serialColumn)

                Label(z,text='   Username   ').grid(row=startRow,column=unColumn)
                
                Label(z,text='   Account   ').grid(row=startRow,column=acColumn)


            un,ac,pas,rem = isolate(i)

            a = isolate(i)            

            Label(z,text=str(counter-startRow),width=7).grid(row=counter,column=serialColumn)

            j = un
            Label(z,text=j).grid(row=counter,column=unColumn)


            j = ac
            Label(z,text=j).grid(row=counter,column=acColumn)

            old = record()

            old.stringToObject(i)

            un = old.un
            ac = old.acc
            pas = old.pas
            rem = old.remarks

            thisrecord = str(old)
            
            Button(z,text='Modify Record',\
                                   command=self.callbackForModify(thisrecord)).grid(row=counter,column=acColumn + 1)

            counter += 1

        for i in self.Lwindows:

            ##check if it is the last window.
            ##if it is not then add a button that says "go te next page"
            
            if not i == self.Lwindows[-1]:
                Button(i,text='See next page',command=i.destroy).grid(row=21,column=2)

            Button(i,text='Back To Main Menu',command=self.reinitialise).grid(row=22,column=2)

        inFile.close()

        self.frame = copy  

    def callbackForModify(self,thisrecord):

        '''returns functions that can be used to modify a record'''

        def callback():

            self.checkpoint()

            self.reinitialise()

            self.window.withdraw()           

            newrec = modRec(thisrecord)

            self.window.deiconify()

            if newrec.isEmpty():
                tkMessageBox.showinfo('warning','all fields of new record are \
empty. we will not make any changes to the file')

                self.window.deiconify()
                return

            if str(newrec) == thisrecord:
                tkMessageBox.showinfo('no changes made','no changes were made \
to the original record. no change will be made in the file')

                self.window.deiconify()
                return

            filin = open(fileName,'r')
            
            filout = open('temp','w')

            filin.seek(0)

            filout.seek(0)

            for i in filin:

                rem = i

                while(rem[-1] == '\r' or rem[-1] == '\n'):

                    rem = rem[:-1]

                remat = thisrecord

                while(remat[-1] == '\r' or remat[-1] == '\n'):

                    remat = remat[:-1]

                if rem == remat:

                    filout.write(str(newrec))
                    
                else:

                    filout.write(i)

            filin.close()

            filout.close()

            self.rearrangeFiles()

            tkMessageBox.showinfo('message','the record was modified')

            self.modify()   

        return callback

    #######################################

##      DELETE ANY ONE ACCOUNT

    #######################################

    def delAcc(self):
        '''will give the user a method to delete any one account
            from a list of accounts'''


        self.getNumRec = self.getnumrec

        self.Lwindows = []

        inFile = open(fileName,'r')

        self.checkpoint()

        startRow = 0
        serialColumn = 1
        unColumn = 2
        acColumn = 3

        counter = startRow + 1

        copy = self.frame    ##storing the current windows frame location
                            ##in memory for further access later.

        for i in inFile:  ##i contains one full record with all the parameters in a record

            if (counter - 1) % 20 == 0:

                y = Toplevel()

                self.Lwindows.append(y)

                z = Frame(y)

                z.grid()

                Label(z,text='   Serial   ',width=7).grid(row=startRow,column=serialColumn)

                Label(z,text='   Username   ').grid(row=startRow,column=unColumn)
                
                Label(z,text='   Account   ').grid(row=startRow,column=acColumn)


            un,ac,pas,rem = isolate(i)

            a = isolate(i)            

            Label(z,text=str(counter-startRow),width=7).grid(row=counter,column=serialColumn)

            j = un
            Label(z,text=j).grid(row=counter,column=unColumn)


            j = ac
            Label(z,text=j).grid(row=counter,column=acColumn)

            old = record()

            old.stringToObject(i)

            un = old.un
            ac = old.acc
            pas = old.pas
            rem = old.remarks

            thisrecord = str(old)
            
            Button(z,text='Delete this Record',\
                                   command=self.callbackForDelete(thisrecord)).grid(row=counter,column=acColumn + 1)

            counter += 1

        for i in self.Lwindows:

            ##check if it is the last window.
            ##if it is not then add a button that says "go te next page"
            
            if not i == self.Lwindows[-1]:
                Button(i,text='See next page',command=i.destroy).grid(row=21,column=2)

            Button(i,text='Back To Main Menu',command=self.reinitialise).grid(row=22,column=2)

        inFile.close()

        self.frame = copy

    def callbackForDelete(self,thisrecord):

        '''returns functions that can be used to delete a record'''

        def callback():

            self.checkpoint()
            
            self.reinitialise()

            inFile = open(fileName,'r')

            out = open('temp','w')

            flag = False  ##flag will be set to true if the user has deleted an account

            for i in inFile:

                rem = i

                while(rem[-1] == '\r' or rem[-1] == '\n'):

                    rem = rem[:-1]

                remat = thisrecord

                while(remat[-1] == '\r' or remat[-1] == '\n'):

                    remat = remat[:-1]

                if rem == remat:                

                    un,ac,pas,rem = isolate(i)

                    message = 'Username:' + un + '\nAccount:' + ac + '\nPassword:'\
                                 + pas + '\nRemarks:' + rem + '\n\n' +\
                    'you have chosen to delete this account. are you sure?'

             
                    if not tkMessageBox.askyesno('confirmation',message):

                        ##user chose not to delete the record                      

                        tkMessageBox.showinfo('confirmed','the record was not deleted')                        

                        break

                    else:

                        flag = True

                        ##user chose to delete the record

                        message = 'Username:' + un + '\nAccount:' + ac + '\nPassw\
ord:'\
                                 + pas + '\nRemarks:' + rem + '\n\n' + \
'This record has now been deleted.'

                        tkMessageBox.showinfo('deleted',message)

                        continue


                out.write(i)                

            out.close()

            inFile.close()

            if flag:
                self.rearrangeFiles()

            else:

                os.remove('temp')             

        return callback


    #####################################

##      NUMBER OF RECORDS STORED

    #####################################

    def showNumRec(self):

        tkMessageBox.showinfo('Number of records','The total number of records \
are: %s' % str(self.getnumrec()))

    def getnumrec(self):

        '''returns the number of records stored in the file'''

        inFile = open(fileName,'r')

        x = 0

        for i in inFile:
            x+=1

        return x

    ##########################

##      CHANGE MASTER KEY

    ##########################

    def changeMastKey(self):

        self.checkpoint()

        attempt1 = tkSimpleDialog.askstring('new master key','Enter the new master key:',show='*')

        if len(attempt1) < 4:
            tkMessageBox.showinfo('failure','minimum length of master key is 4 charachters')
            self.initFrameAndButtons()
            return

        attempt2 = tkSimpleDialog.askstring('confirm new master key','Re-enter the new master key:',show='*')

        if not attempt1 == attempt2:

            tkMessageBox.showinfo('Failure','The two master keys you entered are not the same. \
\nThe master key was not changed. \nTry again.')

            self.initFrameAndButtons()
            return False

        inFile = open('mast','w')

        attempt1 = attempt1 + salt

        att = sha1(attempt1)
        att = att.hexdigest()



        inFile.write(att)

        inFile.close()

        self.initFrameAndButtons() 
        


    ########################################

##      DELETE ALL ACCOUNTS

    #####################################

    def confirmDelete(self):

        '''function that will confirm the delete all records option from the user'''

        self.checkpoint()

        self.frame.destroy()

        self.initFrame()

        if tkMessageBox.askyesno('Confirmation','Are you sure you want to delete all the records?'):
            self.resetAll()

        else:
            self.initFrameAndButtons()

    def resetAll(self):


        '''deletes all the records stored till now, must not be called directly
            must be called only through the confirmDelete function that will
            give the user a choice to delete all the records'''

        inFile = open(fileName,'w')

        inFile.close()

        tkMessageBox.showinfo('confirmation','All the records have been deleted')

        self.initFrameAndButtons()


    ##############################

##      EXITING THE APPLICATION

    ##############################

    def unauthorised(self,ev=None):

        '''will be called if the user enters the wrong master password'''

        self.frame.destroy()
        
        ##Do the essential before the asthetics!

        global flag
        flag = True
        
        os.rename(fileName,'viper')

        encryption.encryptAll()

        self.reinitialise()

        self.initFrameForTableDisplay()

        self.frame.grid_propagate(1)

        self.big  = tkFont.Font(family='helvetica',size=24)

        r = self.frame

        c = 0
        
        Label(r,text='Unauthorised access detected. Goodbye',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='Created by Siddharth Kannan',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='Written on Python 2.7 and Tkinter 8.5',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='OS: LINUX MINT 14 NADIA',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='This software is licensed under the WTFPL license.',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='See the copying file for more details.',font=self.big).grid(row=c,column=0)
        c+=1


    def quitwin(self,event=None):

        '''function that will destroy the present window and then create a new
            window that will give the credits'''

        self.reinitialise()

        self.frame.destroy()

        self.initFrameForTableDisplay()

        self.frame.grid_propagate(1)

        self.big  = tkFont.Font(family='helvetica',size=24)

        r = self.frame

        c = 0

        Label(r,text='Created by Siddharth Kannan',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='Written on Python 2.7 and Tkinter 8.5',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='OS: LINUX MINT 14 NADIA',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='This software is licensed under the WTFPL license.',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='See the copying file for more details.',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='Application will quit in 8 seconds.',font=self.big).grid(row=c,column=0)
        c+=1
        
        ##Do the essential before the asthetics!
        
        os.rename(fileName,'viper')

        global flag
        
        flag = True

        encryption.encryptAll()

        self.window.after(8000,self.window.destroy)
        
        
def main():

	##checking to see if the file is there. If not create a new empty file.


	try:

	    filin = open('viper','r')

	except IOError:

	    filin = open('viper','w')

	filin.close()

	##now encrypt the file. We ensure that the file is there. Even though it may be empty.

	filin = open('viper','r')

	line = filin.readline()

	if not (line.find('username') == -1):  ##if word "username" is there in the line

	    filin.close()

	    encryption.encryptAll()

	encryption.decryptAll()

	##Renaming the file for better safety. Using a '.' before
	##the filename ensures that it remains hidden in unix systems.

	import time
	import hashlib        

	newFileName = '.' + hashlib.sha1(str(time.time())).hexdigest()

	os.rename('viper',newFileName)	
	
	global fileName

	fileName = newFileName

	##there is a possiblity that the user may close the application without
	##pressing the quit button. But by pressin the close button in the top
	##right corner. To handle this we need a flag:

	flag = False  ##if encryption is done then this will be made to True.

	##Inintialising the application
		      
	app = VIPER()

	mainloop()

	if not flag:

	    os.rename(fileName,'viper')

	    encryption.encryptAll()	    

if __name__=='__main__':

	main()	 
