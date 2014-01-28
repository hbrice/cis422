import Tkinter as tk
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
from tkFileDialog import asksaveasfilename
from model import addressbooks
from model import addressbook
from model import contact
from model import address
class AddressBookFrame():

    def __init__(self, master, addressBookLogic):

        self.master = master


        self.frame = tk.Frame(self.master)
        self.frame.grid(row=0,column=0)
        self.contactFrame = tk.Frame(self.frame)
        self.EntryFrame = tk.Frame(self.frame)
        self.buttonFrame = tk.Frame(self.frame)


        #self.logic = addressBookLogic #run
        self.logic = addressbook.addressbook #code

        self.initUI()
        self.buttonFrame.pack(side=tk.BOTTOM, pady=5)
        self.contactFrame.pack(side=tk.LEFT)
        self.EntryFrame.pack(side=tk.LEFT, padx=5)



    def cmdAdd(self):
        #create a new contact based on the contact's name
        self.tempContact = contact.contact(self.entryName.get())
        #build a temp address
        self.tempAddress = address.address(self.entryAddress1.get(),self.entryName.get(),self.entryAddress2.get())
        #add the address to the contact object
        self.tempContact.addAddress(self.tempAddress)
        #get and add the phone number to the contact object
        self.tempContact.addPhoneNumber(self.entryPhone.get())
        #add the contact to the address book
        self.logic.addContact(self.tempContact)
        #add the contact to the contact listbox
        self.contactsList.insert(0,self.entryName.get())

    def cmdRemove(self):
        #remove the selected contact from the address book
        self.logic.removeContactByName(self.contactsList.get(tk.ACTIVE))
        #remove the selected contact from the list box
        self.contactsList.delete(self.contactsList.index(tk.ACTIVE))
        #clear all the entry boxes
        self.entryAddress1.delete(0,tk.END)
        self.entryAddress2.delete(0,tk.END)
        self.entryEmail.delete(0,tk.END)
        self.entryPhone.delete(0,tk.END)
        self.entryName.delete(0,tk.END)


    def cmdSearch(self):
        print "Search"

    def cmdUpdate(self):
        print "Update"
        self.tempContact = self.logic.findContactByName(self.entryName.get())
    def cmdClear(self):
        print "Clear"




    def initUI(self):
        #############################
        #Contact List/contactFrame
        #############################

        #TO-DO add scrollbar, need to make frame to hold listbox and scrollbar then add that frame

        #scrollbar for contactsList
        #sbContactsList = tk.Scrollbar(self.frame)
        #sbContactsList.pack(side=tk.RIGHT, fill=tk.Y)

        #Contacts list
        self.contactsList = tk.Listbox(self.contactFrame, width=25, height=15, selectmode=tk.EXTENDED)
        self.contactsList.grid(row=0, column=0)


        #add scrollbar to contactsList
        #contactsList.config(yscrollcommand=sbContactsList.set)
        #sbContactsList.config(command=contactsList.yview())

        #contactsList.insert(tk.END,"John Smith")
        #contactsList.insert(tk.END,"Jane Smith")

        #############################
        #Entry/entryFrame
        #############################

        #Name
        self.labelName = tk.Label(self.EntryFrame, text="Name")
        self.labelName.grid(row=0,column=0)

        self.entryName = tk.Entry(self.EntryFrame)
        self.entryName.grid(row=1,column=0)

        #Address line 1
        self.labelAddress1 = tk.Label(self.EntryFrame, text="Address Line 1")
        self.labelAddress1.grid(row=2,column=0)

        self.entryAddress1 = tk.Entry(self.EntryFrame)
        self.entryAddress1.grid(row=3,column=0)

        #Address line 2
        self.labelAddress2 = tk.Label(self.EntryFrame, text="Address Line 2")
        self.labelAddress2.grid(row=4,column=0)

        self.entryAddress2 = tk.Entry(self.EntryFrame)
        self.entryAddress2.grid(row=5,column=0)

        #Email
        self.labelEmail = tk.Label(self.EntryFrame, text="Email Address")
        self.labelEmail.grid(row=6,column=0)

        self.entryEmail = tk.Entry(self.EntryFrame)
        self.entryEmail.grid(row=7,column=0)

        #Phone
        self.labelPhone = tk.Label(self.EntryFrame, text="Phone Number")
        self.labelPhone.grid(row=8,column=0)

        self.entryPhone = tk.Entry(self.EntryFrame)
        self.entryPhone.grid(row=9,column=0)

        #############################
        #Buttons/buttonFrame
        #############################
        self.btnAddContact = tk.Button(self.buttonFrame, text="Add", command=self.cmdAdd)
        self.btnAddContact.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.btnRemoveContact = tk.Button(self.buttonFrame, text="Remove", command=self.cmdRemove)
        self.btnRemoveContact.grid(row=0, column=1)

        self.btnUpdateContact = tk.Button(self.buttonFrame, text="Update", command=self.cmdUpdate)
        self.btnUpdateContact.grid(row=0, column=2)

        #Search
        self.entrySearch = tk.Entry(self.buttonFrame, width = 15)
        self.entrySearch.grid(row=1,column=0)

        self.btnSearch = tk.Button(self.buttonFrame, text="Search", command=self.cmdSearch)
        self.btnSearch.grid(row=1,column=1, sticky=tk.W+tk.E)

        self.btnClear = tk.Button(self.buttonFrame, text="Clear", command=self.cmdClear)
        self.btnClear.grid(row=1,column=2, sticky=tk.W+tk.E)



