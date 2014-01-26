__author__ = 'josh'

from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
from tkFileDialog import asksaveasfilename
from view import addressbookgui

root = Tk()
root.geometry("650x500+300+300")

app = addressbookgui.AddressBookFrame(root)
menuBar = Menu(root)

fileMenu = Menu(menuBar, tearoff=0)

def cmdClose():
    print "Close address book"

    #enable menu options
    fileMenu.entryconfig(2,state=DISABLED) #close
    fileMenu.entryconfig(3,state=DISABLED) #Save
    fileMenu.entryconfig(4,state=DISABLED) #Save As
    fileMenu.entryconfig(5,state=DISABLED) #Import
    fileMenu.entryconfig(6,state=DISABLED) #export

def cmdSave():
    print "Save"

def cmdSaveAs():
    newFileName = asksaveasfilename()
    print(newFileName)

def cmdImport():
    openFileName = askopenfilename()
    print(openFileName)

def cmdExport():
    openFileName = askopenfilename()
    print(openFileName)

def cmdQuit():
    sys.exit()

def cmdNew():
    newFileName = asksaveasfilename()
    print(newFileName)
    #take newFileName and create a new AddressBookFrame within AddressBooksFrame

    #enable menu options
    fileMenu.entryconfig(2,state=NORMAL) #close
    fileMenu.entryconfig(3,state=NORMAL) #Save
    fileMenu.entryconfig(4,state=NORMAL) #Save As
    fileMenu.entryconfig(5,state=NORMAL) #Import
    fileMenu.entryconfig(6,state=NORMAL) #export

def cmdOpen():
    openFileName = askopenfilename()
    print(openFileName)
    #take openFileName and create a new AddressBookFrame within AddressBooksFrame

    #enable menu options
    fileMenu.entryconfig(2,state=NORMAL) #close
    fileMenu.entryconfig(3,state=NORMAL) #Save
    fileMenu.entryconfig(4,state=NORMAL) #Save As
    fileMenu.entryconfig(5,state=NORMAL) #Import
    fileMenu.entryconfig(6,state=NORMAL) #export

def main():

    fileMenu.add_command(label="New", command=cmdNew)
    fileMenu.add_command(label="Open", command=cmdOpen)
    fileMenu.add_command(label="Close", command=cmdClose, state=DISABLED)
    fileMenu.add_command(label="Save", command=cmdSave, state=DISABLED)
    fileMenu.add_command(label="Save As", command=cmdSaveAs, state=DISABLED)
    fileMenu.add_command(label="Import", command=cmdImport, state=DISABLED)
    fileMenu.add_command(label="Export", command=cmdExport, state=DISABLED)
    fileMenu.add_command(label="Quit", command=cmdQuit)
    menuBar.add_cascade(label="File", menu=fileMenu)


    root.config(menu=menuBar)

    root.mainloop()


if __name__ == '__main__':
    main()