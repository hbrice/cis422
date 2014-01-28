__author__ = 'josh'

import Tkinter as tk
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
from tkFileDialog import asksaveasfilename
from view import addressbookgui
import sys
from model import addressbooks
from model import addressbook

class AddressBooksFrame():

    def __init__(self, master):
        self.master = master

        #container for ALL the addressbook
        self.books = addressbooks.addressbooks()

       # self.newWindow = tk.Toplevel(self.master)
        self.topFrame = tk.Frame(self.master)
        self.topFrame.pack(side = tk.TOP)
        self.bottomFrame = tk.Frame(self.master)

      #  self.bottomFrame.pack(side = tk.BOTTOM)
        self.bottomFrame.pack(fill=tk.BOTH)

        #add the menubar
        self.menuBar = tk.Menu(self.topFrame)
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
        self.books.save(self.saveFileName)
        print "Save"

    #action for File-->SaveAs
    def cmdSaveAs(self):
        #prompt for a file location
        self.saveFileName = asksaveasfilename()
        #once it's been saved once we can save without prompting
        self.fileMenu.entryconfig(3,state=tk.DISABLED) #Save
        print(self.saveFileName)

    #action for File-->Import
    def cmdImport(self):
        self.openFileName = askopenfilename()
        print(self.openFileName)
        self.mainBook.addressBookImport(self.openFileName,self.app.contactsList)

    #action for File-->Export
    def cmdExport(self):
        self.openFileName = askopenfilename()
        print(self.openFileName)
        #self.mainBook.export(.mainBook.)
        print(self.app.contactsList.curselection())

    #action for File-->Quit
    def cmdQuit(self):
        sys.exit()

    #action for File-->New
    def cmdNew(self):
        try:
            #display dialog for new file
             self.newFileName = asksaveasfilename()
        except:
            print "Error"
            return

        #print the user selected filename
        print(self.newFileName)
        #take newFileName and create a new AddressBookFrame within AddressBooksFrame

        if self.newFileName != "":
            #for now we have a single address book
            self.mainBook = addressbook.addressbook()

            #add the single addressbook to the addressbooks container
            self.books.addAddressBook(self.mainBook)

            self.app = addressbookgui.AddressBookFrame(self.bottomFrame,self.mainBook)

            #enable menu options
            self.fileMenu.entryconfig(2,state=tk.NORMAL) #close
            self.fileMenu.entryconfig(4,state=tk.NORMAL) #Save As
            self.fileMenu.entryconfig(5,state=tk.NORMAL) #Import
            self.fileMenu.entryconfig(6,state=tk.NORMAL) #export

    def cmdOpen(self):
        try:
            #display dialog for new file
             self.openFileName = askopenfilename()
        except:
            print "Error"
            return

        #print the user selected filename
        print(self.openFileName)
        #take newFileName and create a new AddressBookFrame within AddressBooksFrame

        if self.openFileName != "":
            #for now we have a single address book
            self.mainBook = addressbook.addressbook()

            #add the single addressbook to the addressbooks container
            self.books.addAddressBook(self.mainBook)

            self.app = addressbookgui.AddressBookFrame(self.bottomFrame,self.mainBook)

            #enable menu options
            self.fileMenu.entryconfig(2,state=tk.NORMAL) #close
            self.fileMenu.entryconfig(4,state=tk.NORMAL) #Save As
            self.fileMenu.entryconfig(5,state=tk.NORMAL) #Import
            self.fileMenu.entryconfig(6,state=tk.NORMAL) #export

