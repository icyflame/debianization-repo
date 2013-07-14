from Tkinter import *

import tkMessageBox

alert = tkMessageBox.showinfo

import tkFont

SHOW_TOPBAR = True

class CowsAndBulls:

    def __init__(self):

        self.window = Tk()

        self.window.title('Cows and Bulls')

        self.initFrameAndButtons()

        self.initMenu()

        self.initBindings()

        self.makeFullScreen()


    def initBindings(self,event=None):

        w = self.window

        w.bind('n',self.startNewGame)
        w.bind('s',self.seePast)
        w.bind('<Escape>',self.quitwin)

    def initMenu(self,ev=None):

        menubar = Menu(self.window)

        filemenu = Menu(menubar,tearoff = 0)

        filemenu.add_command(label='Start a new game',command=self.startNewGame,accelerator='N')
        filemenu.add_command(label='See performance in older games',command=self.seePast,accelerator='S')
        filemenu.add_command(label='Quit',command=self.quitwin,accelerator='Escape')
        
        helpmenu = Menu(menubar,tearoff=0)

        helpmenu.add_command(label='Help',command=self.showHelp)
        helpmenu.add_command(label='About',command=self.showCredits)

        menubar.add_cascade(label='File',menu=filemenu)
        menubar.add_cascade(label='Help',menu=helpmenu)

        self.window.config(menu=menubar)

    def makeFullScreen(self,ev=None):

        root = self.window

        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.overrideredirect(not SHOW_TOPBAR)
        root.geometry("%dx%d+0+0" % (w, h))

    def initFrame(self,ev=None):

        try:

            self.frame.destroy()

        except:

            pass

        self.frame = Frame(self.window)

        self.frame.pack()

    def initFrameAndButtons(self,ev=None):

        self.initFrame()

        listOfButtons = []

        self.big  = tkFont.Font(family='helvetica',size=24)

        listOfButtons.append(Button(self.frame,text='New game',command=self.startNewGame))
        
        listOfButtons.append(Button(self.frame,text='QUIT',command=self.quitwin,fg='black',bg='red'))

        
        for i in range(len(listOfButtons)):

            listOfButtons[i]['font']=self.big

            listOfButtons[i].pack(side='top')

    def startNewGame(self,ev=None):

        import random

        comp = ''

        comp += str(random.choice(range(1,10,1)))

        for i in range(2):

            comp += str(random.choice(range(10)))

        comp = int(comp)

        self.initFrame()

        self.frame.grid()

        GameOver = False

        f = self.frame

        global counter

        counter = 1

        Label(f,text='Guess',width=15).grid(row=counter,column=1)

        Label(f,text='BULLS',width=15).grid(row=counter,column=2)

        Label(f,text='COWS',width=15).grid(row=counter,column=3)

        counter += 1

        a= StringVar()           

        def validate(ev=None):

            '''function will check if or not the given three digit string
                which is now inside the string var 'a' and will be obtained
                by a.get() is a valid three digit number or not.


                it will first check if there are three digits. if there are then
                it will check if these three characters are digits.

                if both these conditions are satisfied then it will call the function
                done() which will add to the output thus giving useful information
                to the user.

                if not then the relevant error message is shown and then we wait for
                the next input from the user.'''

            flag = True

            guess = str(a.get())

            if not (len(guess) == 3):

                alert('INSTRUCTIONS','YOU DID NOT ENTER A THREE DIGIT NUMBER')

                flag = False

            else:

                try:

                    int(guess)

                except:

                    alert('INSTRUCTIONS','A NUMBER SHOULD HAVE DIGITS ONLY')

                    flag = False

            if flag:

                done()

            else:

                a.set('')

                return


        def done():

            '''this function will be called when it is decided that the user
                entered a valid three digit number.

                this function will check the relevant cows and bulls thing and
                then update the output for the user.'''

            b = str(a.get())

            numbers = [int(i) for i in b]

            compNum = [int(i) for i in str(comp)]

            bulls = 0

            cows = 0


            bulls, cows = bulls_and_cows(b,comp)
            
            if  str(a.get()) == str(comp):

                GameOver = True
                self.gameOver()

            global counter

            Label(f,text=str(a.get())).grid(row=counter,column=1)

            Label(f,text=str(bulls)).grid(row=counter,column=2)

            Label(f,text=str(cows)).grid(row=counter,column=3)

            counter += 1

            a.set('')


        def digits(number):

            '''will return the list of digits in a number'''
            
            return [int(d) for d in str(number)]

        def bulls_and_cows(guess, target):

            '''returns a tuple of the number of bulls and the cows
               when guess is the number that is given by the user and
                target is the number randomly selectedby the computer'''
            
            guess, target = digits(guess), digits(target)
            
            bulls = [d1 == d2 for d1, d2 in zip(guess, target)].count(True)
            
            cows = 0
            
            for digit in set(guess):
                
              cows += min(guess.count(digit), target.count(digit))
              
            return bulls, cows - bulls



        d = Entry(f,textvariable=a,width=3)

        d.grid(row=0,column=0)

        d.focus()        
        
        self.window.bind('<Return>',validate)

        Button(f,text='submit',command=validate).grid(row=0,column=1)

        Button(f,text='End game',command=self.checkAll).grid(row=0,column=2)

        Button(f,text='Main Menu',command=self.initFrameAndButtons).grid(row=0,column=3)


    def checkAll(self):

        import tkMessageBox


        if tkMessageBox.askyesno('Are you sure?','If you exit now, then you will forfeit this game automatically. Are you sure you want to exit?'):

            self.win('c')

            self.initFrameAndButtons()


        else:


            return
                                                                

    def gameOver(self,ev=None):

        alert('Game over','Congrats! you win!')

        self.win('u')

        self.initFrameAndButtons()


    def win(self,param):

        import time

        form = '%B %d, %Y, %H:%M:%S'

        filin = open('past.txt','a')

        filin.write(time.strftime(form) + '  ')

        if param == 'c':

            filin.write('Computer won this game')

        if param == 'u':

            filin.write('User won this game')

        filin.write('\n')

        filin.close()


    def seePast(self):

        pass

    def showHelp(self,ev=None):

        pass


    def showCredits(self,ev=None):

        pass
            

    def quitwin(self,ev=None):

        self.window.destroy()

        self.initFrame()

        self.frame.grid()

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

##        self.window.after(8000,self.window.destroy)

CowsAndBulls()

mainloop()       

