__author__ = 'josh'

import Tkinter as tk
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
from tkFileDialog import asksaveasfilename
import addressbookgui
import sys
import addressbook
import tkMessageBox

class AddressBooksFrame():

    def __init__(self, master):
        """keep a record of the calling parent object"""
        self.master = master

        """container for ALL the addressbook"""
        self.books = addressbook.addressbook()

        """setup frames for the menu bar and the area below it"""
        self.topFrame = tk.Frame(self.master)
        self.topFrame.pack(side = tk.TOP)
        self.bottomFrame = tk.Frame(self.master)
        self.bottomFrame.pack(fill=tk.BOTH)

        """add the menubar to the upper frame"""
        self.menuBar = tk.Menu(self.topFrame)
        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)

        """set the default states for the file menu"""
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

        """add the menu bar"""
        self.master.config(menu=self.menuBar)

    """action for File-->Close"""
    def cmdClose(self):
        """check for unsaed changes"""
        if self.app.unSavedChanges == 1:
            result = tkMessageBox.askquestion("Unsaved","You have unsaved changes in the address book, are you sure you want to close it?")
            if result == 'no':
                return

        """remove the container frame"""
        self.app.frame.grid_forget()
        """we won't need any pointer to app so destroy"""
        self.app.frame.destroy()

        """enable new & open"""
        self.fileMenu.entryconfig(0,state=tk.NORMAL) #new
        self.fileMenu.entryconfig(1,state=tk.NORMAL) #open

        """disable menu options"""
        self.fileMenu.entryconfig(2,state=tk.DISABLED) #close
        self.fileMenu.entryconfig(3,state=tk.DISABLED) #Save
        self.fileMenu.entryconfig(4,state=tk.DISABLED) #Save As
        self.fileMenu.entryconfig(5,state=tk.DISABLED) #Import
        self.fileMenu.entryconfig(6,state=tk.DISABLED) #export
        self.fileMenu.entryconfig(7,state=tk.DISABLED) #print
        self.fileMenu.entryconfig(8,state=tk.DISABLED) #merge


    """action for File-->Save"""
    def cmdSave(self):
        """if the filename is not blank"""
        if self.saveFileName != "":
            """write the file to the pre-established (by save-as) file"""
            self.mainBook.export(self.mainBook.contacts,self.saveFileName)
            """no unsaved changes"""
            self.app.unSavedChanges = 0

    """action for File-->SaveAs"""
    def cmdSaveAs(self):
        try:
            #prompt for a file location
            self.saveFileName = asksaveasfilename()
        except:
            print "Save As error"

        """if the filename is not blank"""
        if self.saveFileName != "":
            """once it's been saved once we can save without prompting"""
            self.fileMenu.entryconfig(3,state=tk.NORMAL) #Save
            """call the save function"""
            self.mainBook.export(self.mainBook.contacts,self.saveFileName)
            """no unsaved changes"""
            self.app.unSavedChanges = 0

    """action for File-->Import"""
    def cmdImport(self):
        """get the filename"""
        self.openFileName = askopenfilename()
        """try importing"""
        self.mainBook.addressBookImport(self.openFileName,self.app)

    """action for File-->Export"""
    def cmdExport(self):
        self.exportFileName = asksaveasfilename()

        if self.exportFileName != "":
            """get the selection and export it to the selected file"""
            tempContacts = []
            for x in self.app.contactsList.curselection():
                tempContacts.append(self.app.contactPairs[int(x)+1])
            """pass the seletion to export"""
            self.mainBook.export(tempContacts,self.exportFileName)

    """action for File-->Print, this print out all the contacts in mailing label format"""
    def cmdPrint(self):
        self.exportFileName = asksaveasfilename()

        if self.exportFileName != "":
            f = open(self.exportFileName, 'w')
            for x in self.mainBook.contacts:
                """print a contact"""
                f.write(x.mailingFormat())
                """spacing between each contact"""
                f.write("\n\n")
            f.close

    """action for file-->merge"""
    def cmdMerge(self):
        print "merge"
        self.openFileName = askopenfilename()

        if self.openFileName != "":
            """setup the backend addressbook"""
            self.newBook = addressbook.addressbook()
            self.newBook.addressBookImport(self.openFileName,self.app)
            self.mainBook.mergeAddressBook(self.newBook)
            self.app.cmdUpdateListbox(self.mainBook.contacts)

    """action for File-->Quit"""
    def cmdQuit(self):
        """if there's an addressbook open"""
        if hasattr(self, 'app'):
            """check for unsaved work"""
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
        """setup out backend addressbook"""
        self.mainBook = addressbook.addressbook()
        """setup the GUI and pass in the addressbook backend"""
        self.app = addressbookgui.AddressBookFrame(self.bottomFrame,self.mainBook)

        """enable menu options"""
        self.fileMenu.entryconfig(2,state=tk.NORMAL) #close
        self.fileMenu.entryconfig(4,state=tk.NORMAL) #Save As
        self.fileMenu.entryconfig(5,state=tk.NORMAL) #Import
        self.fileMenu.entryconfig(6,state=tk.NORMAL) #export
        self.fileMenu.entryconfig(7,state=tk.NORMAL) #print
        self.fileMenu.entryconfig(8,state=tk.NORMAL) #merge

        """disable new & open"""
        self.fileMenu.entryconfig(0,state=tk.DISABLED) #new
        self.fileMenu.entryconfig(1,state=tk.DISABLED) #open

    """action for file-->open"""
    def cmdOpen(self):
        """display dialog for load file"""
        self.openFileName = askopenfilename()

        if self.openFileName != "":
            """setup the backend addressbook"""
            self.mainBook = addressbook.addressbook()
            """setup the GUI addressbook frame"""
            self.app = addressbookgui.AddressBookFrame(self.bottomFrame,self.mainBook)
            """open the selected file into our addressbook"""
            self.mainBook.addressBookImport(self.openFileName,self.app)
            """disable new & open"""
            self.fileMenu.entryconfig(0,state=tk.DISABLED) #new
            self.fileMenu.entryconfig(1,state=tk.DISABLED) #open

            """enable menu options"""
            self.fileMenu.entryconfig(2,state=tk.NORMAL) #close
            self.fileMenu.entryconfig(4,state=tk.NORMAL) #Save As
            self.fileMenu.entryconfig(5,state=tk.NORMAL) #Import
            self.fileMenu.entryconfig(6,state=tk.NORMAL) #export
            self.fileMenu.entryconfig(7,state=tk.NORMAL) #print
            self.fileMenu.entryconfig(8,state=tk.NORMAL) #merge

