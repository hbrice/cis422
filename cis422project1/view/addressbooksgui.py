__author__ = 'josh'

import Tkinter as tk
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
from tkFileDialog import asksaveasfilename
from view import addressbookgui
import sys
from model import addressbook
import tkMessageBox
import pickle

class AddressBooksFrame():

    def __init__(self, master):
        self.master = master

        #container for ALL the addressbook
        self.books = addressbook.addressbook()

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
        self.fileMenu.add_command(label="Print Mailing", command=self.cmdPrint, state=tk.DISABLED)
        self.fileMenu.add_command(label="Merge", command=self.cmdMerge, state=tk.DISABLED)
        self.fileMenu.add_command(label="Quit", command=self.cmdQuit)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

        self.master.config(menu=self.menuBar)

    #action for File-->Close
    def cmdClose(self):
        print "Close address book"
        if self.app.unSavedChanges == 1:
            result = tkMessageBox.askquestion("Unsaved","You have unsaved changes in the address book, are you sure you want to close it?")
            if result == 'no':
                return

        #remove the container frame
        self.app.frame.grid_forget()
        #we won't need any pointer to is so destroy
        self.app.frame.destroy()

        #enable new & open
        self.fileMenu.entryconfig(0,state=tk.NORMAL) #new
        self.fileMenu.entryconfig(1,state=tk.NORMAL) #open

        #disable menu options
        self.fileMenu.entryconfig(2,state=tk.DISABLED) #close
        self.fileMenu.entryconfig(3,state=tk.DISABLED) #Save
        self.fileMenu.entryconfig(4,state=tk.DISABLED) #Save As
        self.fileMenu.entryconfig(5,state=tk.DISABLED) #Import
        self.fileMenu.entryconfig(6,state=tk.DISABLED) #export
        self.fileMenu.entryconfig(7,state=tk.DISABLED) #print
        self.fileMenu.entryconfig(8,state=tk.DISABLED) #merge


    #action for File-->Save
    def cmdSave(self):
        #if the filename is not blank
        if self.saveFileName != "":
            self.mainBook.export(self.mainBook.contacts,self.saveFileName)
            self.app.unSavedChanges = 0

    #action for File-->SaveAs
    def cmdSaveAs(self):
        try:
            #prompt for a file location
            self.saveFileName = asksaveasfilename()
        except:
            print "Save As error"

        #if the filename is not blank
        if self.saveFileName != "":
            #once it's been saved once we can save without prompting
            self.fileMenu.entryconfig(3,state=tk.NORMAL) #Save
            #call the save function
            #self.books.save(self.saveFileName)
            self.mainBook.export(self.mainBook.contacts,self.saveFileName)
            self.app.unSavedChanges = 0

    #action for File-->Import
    def cmdImport(self):
        self.openFileName = askopenfilename()
        print(self.openFileName)
        self.mainBook.addressBookImport(self.openFileName,self.app)

    #action for File-->Export
    def cmdExport(self):
        self.exportFileName = asksaveasfilename()

        if self.exportFileName != "":
            tempContacts = []
            for x in self.app.contactsList.curselection():
                tempContacts.append(self.app.contactPairs[int(x)+1])

            self.mainBook.export(tempContacts,self.exportFileName)

    def cmdPrint(self):
        self.exportFileName = asksaveasfilename()

        if self.exportFileName != "":
            f = open(self.exportFileName, 'w')
            for x in self.mainBook.contacts:
                #print >> f, x
                f.write(x.mailingFormat())
                f.write("\n\n")
            f.close

    def cmdMerge(selfself):

        print "merge"

    #action for File-->Quit
    def cmdQuit(self):
        if hasattr(self, 'app'):
            if self.app.unSavedChanges == 1:
                result = tkMessageBox.askquestion("Unsaved","You have unsaved changes in the address book, are you sure you want to quit?")
                if result == 'yes':
                    sys.exit()
                else:
                    return
            else:
                #close the whole program
                sys.exit()
        else:
            sys.exit()

    #action for File-->New
    def cmdNew(self):
        #for now we have a single address book
        self.mainBook = addressbook.addressbook()

        #add the single addressbook to the addressbooks container
        #self.books.addAddressBook(self.mainBook)

        self.app = addressbookgui.AddressBookFrame(self.bottomFrame,self.mainBook)

        #enable menu options
        self.fileMenu.entryconfig(2,state=tk.NORMAL) #close
        self.fileMenu.entryconfig(4,state=tk.NORMAL) #Save As
        self.fileMenu.entryconfig(5,state=tk.NORMAL) #Import
        self.fileMenu.entryconfig(6,state=tk.NORMAL) #export
        self.fileMenu.entryconfig(7,state=tk.NORMAL) #print
        self.fileMenu.entryconfig(8,state=tk.NORMAL) #merge

        #disable new & open
        self.fileMenu.entryconfig(0,state=tk.DISABLED) #new
        self.fileMenu.entryconfig(1,state=tk.DISABLED) #open


    def cmdOpen(self):
        #display dialog for load file
        self.openFileName = askopenfilename()

        if self.openFileName != "":
            self.mainBook = addressbook.addressbook()
            self.app = addressbookgui.AddressBookFrame(self.bottomFrame,self.mainBook)
            self.mainBook.addressBookImport(self.openFileName,self.app)
            #disable new & open
            self.fileMenu.entryconfig(0,state=tk.DISABLED) #new
            self.fileMenu.entryconfig(1,state=tk.DISABLED) #open

            #enable menu options
            self.fileMenu.entryconfig(2,state=tk.NORMAL) #close
            self.fileMenu.entryconfig(4,state=tk.NORMAL) #Save As
            self.fileMenu.entryconfig(5,state=tk.NORMAL) #Import
            self.fileMenu.entryconfig(6,state=tk.NORMAL) #export
            self.fileMenu.entryconfig(7,state=tk.NORMAL) #print
            self.fileMenu.entryconfig(8,state=tk.NORMAL) #merge

