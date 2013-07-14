##File number 1

##This file takes care of taking a new record from the user.

##This is part of the VIPER Program in Python Tkinter

##created on 5th April, 2013

##modified 7th April, 2013

##modified 9th April, 2013
##
##    changes: changed the way that the record is diaplayed as a string.
##
##    now there are no spaces and one full record will be stored in one line
##    and while reading we can use the isolate function that is defined inside
##    the file isolating.py
##
##Modified 20th May, 2013
##
##    changes:
##
##        during the creation of VIPER 5, in the phase where we had to
##        show details in different windows. Lots of debugging code needed to be added.
##        in the main file and here too. That was added and removed.


from Tkinter import *

from isolating import *

SHOW_TOPBAR = True

class record(object):
    def __init__(self,un='',acc='',password='',remarks=''):

        self.un = un
        self.acc = acc
        self.pas = password
        self.remarks = remarks

    def getFromUser(self):

        self.win = Toplevel()

        root = self.win

        # make it cover the entire screen
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.overrideredirect(not SHOW_TOPBAR)
        root.geometry("%dx%d+0+0" % (w, h))

        win = self.win

        win.title('New Record')

        welcome = Frame(win)
        welcome.grid()

        welcomeMessage = Label(welcome,text='This interface will help you enter a new record into the \
VIPER database')

        welcomeMessage.grid()

        Label(welcome,text='\n').grid()

        root = Frame(win,width = 500,height=500)
        root.grid()
        root.grid_propagate(1)

        username = Entry(root,width = 100)

        account = Entry(root,width = 100)

        pw = Entry(root,show='*',width = 100)

        remarks = Entry(root,width = 100)

        userName = Label(root,text='Username:')
        accountName = Label(root,text='Account:')
        pwLabel = Label(root,text='Password:')
        remarksLabel = Label(root,text='Remarks:')

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

        self.un = username.get()
        self.acc = account.get()
        self.pas = pw.get()
        self.remarks = remarks.get()

        win.destroy()

    def copy(self):
        return record(self.un,self.acc,self.pas,self.remarks)

    def __str__(self):
        return 'username:' + str(self.un) + 'account:' + str(self.acc) \
               + 'password:' + self.pas + 'remarks:' + self.remarks + '\n'

    def stringToObject(self,a):
            '''this function will change the given string into the equivalent
                    record object

        a -- string containing the object but in its string form rather than in the object form'''

            if not type(a) == str:
                ols = record()
                if type(a) == type(record):
                    a = str(a)

                else:
                    return

            import isolating

            a = a.strip('\n')

            ##print 'inside string to object:',a

            self.un,self.acc,self.pas,self.remarks = isolating.isolate(a)

    def isEmpty(self):

        '''function will return true if the given record is empty'''

        i = str(self)

        a = isolate(i)

        for x in a:
            if not x =='':
                return False

        return True


########################################################################################
##script level testing code

##print f,l,a,r

##app = record()
##
##print app
##
##out = open('viper','a')
##
##out.write(str(app))
##
##out.close()
