__author__ = 'josh'

import Tkinter as tk
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
from tkFileDialog import asksaveasfilename
from view import addressbookgui
import sys
from model import addressbooks

class AddressBooksFrame():
    def __init__(self, master, logicObject):
        self.master = master
        self.logic = logicObject
        self.frame = tk.Frame(self.master)

        #add the menubar
        self.menuBar = tk.Menu(self.frame)
        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)

        #set the default states for the file
        self.fileMenu.add_command(label="New", command=self.cmdNew)
        self.fileMenu.add_command(label="Open", command=self.cmdOpen)
        self.fileMenu.add_command(label="Close", command=self.cmdClose, state=tk.DISABLED)
        self.fileMenu.add_command(label="Save", command=self.cmdSave, state=tk.DISABLED)
        self.fileMenu.add_command(label="Save As", command=self.cmdSaveAs, state=tk.DISABLED)
        self.fileMenu.add_command(label="Import", command=self.cmdImport, state=tk.DISABLED)
        self.fileMenu.add_command(label="Export", command=self.cmdExport, state=tk.DISABLED)
        self.fileMenu.add_command(label="Quit", command=self.cmdQuit)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

        self.master.config(menu=self.menuBar)

    #action for File-->Close
    def cmdClose(self):
        print "Close address book"

        #enable menu options
        self.fileMenu.entryconfig(2,state=tk.DISABLED) #close
        self.fileMenu.entryconfig(3,state=tk.DISABLED) #Save
        self.fileMenu.entryconfig(4,state=tk.DISABLED) #Save As
        self.fileMenu.entryconfig(5,state=tk.DISABLED) #Import
        self.fileMenu.entryconfig(6,state=tk.DISABLED) #export

    #action for File-->Save
    def cmdSave(self):
        print "Save"

    #action for File-->SaveAs
    def cmdSaveAs(self):
        self.newFileName = asksaveasfilename()
        print(self.newFileName)

    #action for File-->Import
    def cmdImport(self):
        self.openFileName = askopenfilename()
        print(self.openFileName)

    #action for File-->Export
    def cmdExport(self):
        self.openFileName = askopenfilename()
        print(self.openFileName)

    #action for File-->Quit
    def cmdQuit(self):
        sys.exit()

    #action for File-->New
    def cmdNew(self):
        #display dialog for new file
        self.newFileName = asksaveasfilename()

        #print the user selected filename
        print(self.newFileName)
        #take newFileName and create a new AddressBookFrame within AddressBooksFrame

        #enable menu options
        self.fileMenu.entryconfig(2,state=tk.NORMAL) #close
        self.fileMenu.entryconfig(3,state=tk.NORMAL) #Save
        self.fileMenu.entryconfig(4,state=tk.NORMAL) #Save As
        self.fileMenu.entryconfig(5,state=tk.NORMAL) #Import
        self.fileMenu.entryconfig(6,state=tk.NORMAL) #export

    def cmdOpen(self):
         #display dialog for new file
        openFileName = askopenfilename()

        #print the user selected filename
        print(openFileName)
        #take openFileName and create a new AddressBookFrame within AddressBooksFrame

        #enable menu options
        self.entryconfig(2,state=tk.NORMAL) #close
        self.entryconfig(3,state=tk.NORMAL) #Save
        self.entryconfig(4,state=tk.NORMAL) #Save As
        self.entryconfig(5,state=tk.NORMAL) #Import
        self.entryconfig(6,state=tk.NORMAL) #export

