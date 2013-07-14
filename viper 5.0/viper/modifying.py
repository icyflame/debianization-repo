##File number 3

##This file controls all the operations that are related to modifying a record
##
##This is a part of the VIPER program in Python Tkinter
##
##created 11th April, 2013
##
##
##Modified 20th May, 2013
##
##    changes:
##
##        during the creation of VIPER 5, in the phase where we had to
##        show details in different windows. Lots of debugging code needed to be added.
##        in the main file and here too. That was added and removed.


from newRec import *

from tkSimpleDialog import *

from isolating import *

from Tkinter import *

class modifyRecord(object):

    def __init__(self):

        self.win = Toplevel()

        root = self.win

        # make it cover the entire screen
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.overrideredirect(not SHOW_TOPBAR)
        root.geometry("%dx%d+0+0" % (w, h))

        self.old = record()

        self.new = record()

    def modify(self,record1=None):

        '''to modify a record. record1 is the object containing the record'''

        if not record1 == None:

            self1 = record1

            other = self.old

            other.un = self1.un
            other.acc = self1.acc
            other.pas = self1.pas
            other.remarks = self1.remarks

            
            other = self.new

            other.un = self1.un
            other.acc = self1.acc
            other.pas = self1.pas
            other.remarks = self1.remarks

        win = self.win

        win.title('New Record')

        welcome = Frame(win)
        welcome.grid()

        welcomeMessage = Label(welcome,text='This interface will help you enter a new record into the \
VIPER database \n\n To retain the value of any field enter \'.\'(period) \
in place of \
the new value of that field.')

        welcomeMessage.grid()

        Label(welcome,text='\n').grid()

        root = Frame(win,width = 500,height=500)
        root.grid()
        root.grid_propagate(1)

        username = Entry(root,width = 100)

        account = Entry(root,width = 100)

        pw = Entry(root,show='*',width = 100)

        remarks = Entry(root,width = 100)

        userName = Label(root,text='Old Username:' + self.old.un + '  New username')
        accountName = Label(root,text='Old account:' + self.old.acc + '  New account')
        pwLabel = Label(root,text='Old password:' + self.old.pas + '  New password')
        remarksLabel = Label(root,text='Old remarks:' + self.old.remarks + '  New remarks')
        
        userName.grid(row=0,column=0)
        accountName.grid(row=1,column=0)
        pwLabel.grid(row=2,column=0)
        remarksLabel.grid(row=3,column=0)


        username.grid(row=0,column=1)
        account.grid(row=1,column=1)
        pw.grid(row=2,column=1)
        remarks.grid(row=3,column=1)

        b = Button(root,text='Store Record',command=root.quit)

        b.grid(row=4,column=1)

        username.focus_set()

        win.mainloop()

        n = record()        

        n.un = username.get()
        n.acc = account.get()
        n.pas = pw.get()
        n.remarks = remarks.get()

        if n.un =='.':
            n.un = self.old.un

        if n.acc == '.':
            n.acc = self.old.acc

        if n.pas == '.':
            n.pac = self.old.pas

        if n.remarks == '.':
            n.remarks = self.old.remarks

        self.new = n

        self.win.destroy()

        return self.new


################################################################################
##Script level testing code
##
##
##thisRecord = ''
##
##inFile = open('viper','r')
##
##for i in inFile:
##    thisRecord = i
##    break
##
##
##old = record()
##
##print 'record as read from file:',thisRecord
##
##print thisRecord[-1]
##
##old.stringToObject(thisRecord)
##
##newRec = record()
##
##temp = modifyRecord()
##
##newRec = temp.modify(old)
##
###newRecord = a.modify(thisRecord)
##
##inFile.close()
##
###print newRecord
##print 'as in the script level:',newRec
##


def modRec(thisRec):
    '''thisRec is the string that consists of the present record

        will return a record instance that has been modified'''

    old = record()
    
    if type(thisRec) == type('string'):

        old.stringToObject(thisRec)

    newRec = record()

    temp = modifyRecord()

    newRec = temp.modify(old)

    return newRec


##################################################################################
##script level debugging code
##
##infile = open('viper')
##
##string = ''
##
##for i in infile:
##    string = i
##    break
##
##newRec = modRec(string)
##
##print newRec 
    
