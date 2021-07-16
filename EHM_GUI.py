import tkinter as tk
from tkinter import *

#def addEnemyToList():
    
    #global newEnemyHP
    #newEnemyName = 

def addEnemyOpen():
    root_addEnemyWin = Toplevel(root) #open child window
    root_addEnemyWin.geometry("300x80") #size of window
    root_addEnemyWin.title("Add Enemy") #title of window
    
    global addEnemyNameEntry    #Make the two entry boxes global variables
    global addEnemyHPEntry

    addEnemyNameLabel = tk.Label(root_addEnemyWin, text = "Enter enemy name: ")
    addEnemyHPLabel = tk.Label(root_addEnemyWin, text = "Enter enemy HP: ")
    
    addEnemyNameEntry = Entry(root_addEnemyWin)
    addEnemyHPEntry = Entry(root_addEnemyWin)
    
    doneButton = tk.Button(root_addEnemyWin, text="Add enemy")
    

    addEnemyNameLabel.place(bordermode=OUTSIDE,relx = 0.1, rely = 0.1)
    addEnemyNameEntry.place(bordermode=OUTSIDE,relx = 0.5, rely = 0.1)
    addEnemyHPLabel.place(bordermode=OUTSIDE, relx = 0.1, rely = 0.4)
    addEnemyHPEntry.place(bordermode=OUTSIDE, relx = 0.5, rely = 0.4)
    doneButton.pack(side=BOTTOM)


root = tk.Tk()

#size and position of main window
root.geometry('600x400+50+50')
#format - root.geometry('{width}x{height}{+/- position from left screen edge}{+/- position from top screen edge}')
root.resizable(False, True) #keeps size fixed

#Create title of window
root.title("Joe's Enemy Health Manager")

#addEnemyLabel = Label(root,text="Add Enemy name ")
#addEnemyEntry = Entry(root)
addEnemyButton = tk.Button(root, text="Add Enemy", command = addEnemyOpen)
addEnemyButton.pack()



    #place message inside window
    #message = tk.Label(root,text="Hello World!")
    #message.pack()      #make the message visible
#addEnemyLabel.pack()
#addEnemyEntry.pack()
#keep window displaying
root.mainloop()