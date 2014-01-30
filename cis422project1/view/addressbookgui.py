import Tkinter as tk
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
from tkFileDialog import asksaveasfilename
from model import addressbooks
from model import addressbook
from model import contact
from model import address
import tkMessageBox
# noinspection PyInterpreter
class AddressBookFrame():

    def __init__(self, master, addressBookLogic):

        self.unSavedChanges = 0
        self.unUpdated = 0

        self.svName = tk.StringVar()
        self.svLast = tk.StringVar()
        self.svDelivery = tk.StringVar()
        self.svSecond = tk.StringVar()
        self.svEmail = tk.StringVar()
        self.svPhone = tk.StringVar()

        self.svName.trace("w", self.entryChanged)
        self.svLast.trace("w", self.entryChanged)
        self.svDelivery.trace("w", self.entryChanged)
        self.svSecond.trace("w", self.entryChanged)
        self.svEmail.trace("w", self.entryChanged)
        self.svPhone.trace("w", self.entryChanged)


        testContact1 = contact.contact("John Doe")
        testLast1 = "Alameda CA 9"
        testDelivery1 = "1401 SW Main St."
        testSecond1 = "Apt 4"
        testAddr1 = address.address(testLast1, testDelivery1, testSecond1)
        testEmail1 = "jdoe@gmail.com"
        testEmail2 = "doe@uoregon.edu"
        testPhoneNumber1 = "542-345-6745"
        testContact1.addAddress(testAddr1)
        testContact1.addEmail(testEmail1)
        testContact1.addEmail(testEmail2)
        testContact1.addPhoneNumber(testPhoneNumber1)

        testContact2 = contact.contact("Mary Sue")
        testLast2 = "Venice CA 1"
        testDelivery2 = "56 Trent St."
        testSecond2 = ""
        testAddr2 = address.address(testLast2, testDelivery2, testSecond2)
        testEmail2_1 = "marys@gmail.com"
        testEmail2_2 = "msue@uoregon.edu"
        testPhoneNumber2 = "542-524-5820"
        testContact2.addAddress(testAddr2)
        testContact2.addEmail(testEmail2_1)
        testContact2.addEmail(testEmail2_2)
        testContact2.addPhoneNumber(testPhoneNumber2)

        testContact3 = contact.contact("Eddy Adams")
        testLast3 = "Oakland CA 0"
        testDelivery3 = "345 Alder St."
        testSecond3 = ""
        testAddr3 = address.address(testLast3, testDelivery3, testSecond3)
        testEmail3_1 = "erodgers@gmail.com"
        testEmail3_2 = "reddy@uoregon.edu"
        testPhoneNumber3 = "233-595-9090"
        testContact3.addAddress(testAddr3)
        testContact3.addEmail(testEmail3_1)
        testContact3.addEmail(testEmail3_2)
        testContact3.addPhoneNumber(testPhoneNumber3)

        addressBookLogic.addContact(testContact1)
        addressBookLogic.addContact(testContact2)
        addressBookLogic.addContact(testContact3)

        self.master = master

        self.frame = tk.Frame(self.master)
        self.frame.grid(row=0,column=0)
        self.contactFrame = tk.Frame(self.frame)
        self.EntryFrame = tk.Frame(self.frame)
        self.buttonFrame = tk.Frame(self.frame)

        self.entryChanged = 0

        self.logic = addressBookLogic #run
        #self.logic = addressbook.addressbook #code

        self.initUI()
        self.buttonFrame.pack(side=tk.BOTTOM, pady=5)
        self.contactFrame.pack(side=tk.LEFT)
        self.EntryFrame.pack(side=tk.LEFT, padx=5)
        self.cmdUpdateListbox(self.logic.contacts)
        self.contactPairs

    def checkUpdated(self):
        if self.unUpdated == 1:
            result = tkMessageBox.askquestion("Unsaved","You have unsaved changes for the selected contact, are you sure you want to continue?")
            if result == 'no':
                return 0
            else:
                return 1
                self.unUpdated = 0
        return 1


    def entryChanged(self, *args):
        self.unUpdated = 1

    """function that is bound the the listbox selection"""
    def onSelect(self, evt):
        if self.checkUpdated() == 0:
            return

        w = evt.widget
        index = int(w.curselection()[0]) + 1
        tmpContact = self.contactPairs[index]
        self.entryName.delete(0,tk.END)
        self.entryName.insert(0, tmpContact.fname + " " + tmpContact.lname)

        self.entryAddressLast.delete(0,tk.END)
        self.entryAddressLast.insert(0, tmpContact.addressList[0].last)

        self.entryAddressDelivery.delete(0,tk.END)
        self.entryAddressDelivery.insert(0, tmpContact.addressList[0].delivery)

        self.entryAddressSecond.delete(0,tk.END)
        self.entryAddressSecond.insert(0, tmpContact.addressList[0].second)

        self.entryEmail.delete(0,tk.END)
        if len(tmpContact.emailList) > 0:
            self.entryEmail.insert(0, tmpContact.emailList[0])

        self.entryPhone.delete(0,tk.END)
        if len(tmpContact.phoneNumberList) > 0:
            self.entryPhone.insert(0, tmpContact.phoneNumberList[0])

        self.unUpdated = 0


    def cmdAdd(self):
        #create a new contact based on the contact's name
        self.tempContact = contact.contact(self.entryName.get())
        #build a temp address
        self.tempAddress = address.address(self.entryAddressLast.get(),self.entryAddressDelivery.get(),self.entryAddressSecond.get())
        #add the address to the contact object
        self.tempContact.addAddress(self.tempAddress)
        #add the email address to the contact object
        self.tempContact.addEmail(self.entryEmail.get())
        #get and add the phone number to the contact object
        self.tempContact.addPhoneNumber(self.entryPhone.get())
        #add the contact to the address book
        self.logic.addContact(self.tempContact)
        #update the listbox
        self.cmdUpdateListbox(self.logic.contacts)

        self.unSavedChanges = 1

    def cmdRemove(self):
        tmpSelection = self.contactsList.curselection()
        if len(tmpSelection) > 0:
            tmpIndex = int(tmpSelection[0])
            tmpIndex=tmpIndex+1
            print tmpIndex
            if len(tmpSelection) > 1:
                tkMessageBox.showinfo("Too Many!", "Too many entries selected, please remove one at a time.")
            else:
                tempContact = self.contactPairs[tmpIndex]
                #remove the contact
                self.logic.removeContact(tempContact)

                #clear all the entry boxes
                self.entryAddressSecond.delete(0,tk.END)
                self.entryAddressDelivery.delete(0,tk.END)
                self.entryAddressLast.delete(0,tk.END)
                self.entryEmail.delete(0,tk.END)
                self.entryPhone.delete(0,tk.END)
                self.entryName.delete(0,tk.END)
                self.cmdUpdateListbox(self.logic.contacts)
                self.unSavedChanges = 1
        else:
            tkMessageBox.showinfo("Not enough!", "No entries selected.")


    def cmdNameSearch(self):
        if self.checkUpdated() == 0:
            return

        print "Name Search"
        query = self.entrySearch.get()
        if query != "":
            results=self.logic.findContactByName(query)
            if results != []:
                self.cmdUpdateListbox(results)
            else:
                self.cmdClearListBox


    def cmdGeneralSearch(self):
        if self.checkUpdated() == 0:
            return

        print "General Search"
        query = self.entrySearch.get()
        if query != "":
            results=self.logic.generalSearchContacts(query)
            if results != []:
                self.cmdUpdateListbox(results)
            else:
                self.cmdClearListBox

    def cmdUpdate(self):
        print "Update"
        tmpSelection = self.contactsList.curselection()
        if len(tmpSelection) > 0:
            tmpIndex = int(tmpSelection[0])
            tmpIndex=tmpIndex+1
            print tmpIndex
            if len(tmpSelection) > 1:
                tkMessageBox.showinfo("Too Many!", "Too many entries selected, please update one at a time.")
            else:
                tempContact = self.contactPairs[tmpIndex]
                #remove the contact
                self.logic.removeContact(tempContact)
                #add the contact back in with the updated info
                self.cmdAdd()
                self.unSavedChanges = 1
        else:
            tkMessageBox.showinfo("Not enough!", "No entries selected.")

    def cmdClear(self):
        if self.checkUpdated() == 0:
            return

        print "Clear"
        self.entrySearch.delete(0,tk.END)
        self.cmdUpdateListbox(self.logic.contacts)

    def cmdClearContact(self):
        if self.checkUpdated() == 0:
            return

        #clear all the entry boxes
        self.entryAddressSecond.delete(0,tk.END)
        self.entryAddressDelivery.delete(0,tk.END)
        self.entryAddressLast.delete(0,tk.END)
        self.entryEmail.delete(0,tk.END)
        self.entryPhone.delete(0,tk.END)
        self.entryName.delete(0,tk.END)

    def cmdSortName(self):
        if self.checkUpdated() == 0:
            return

        print "sort by last name"
        self.logic.sortByLname()
        self.cmdUpdateListbox(self.logic.contacts)

    def cmdSortZIP(self):
        if self.checkUpdated() == 0:
            return

        print "sort by ZIP"
        self.logic.sortByZip()
        self.cmdUpdateListbox(self.logic.contacts)

    def cmdClearListBox(self):
        if self.checkUpdated() == 0:
            return
        self.contactsList.delete(0,tk.END)

    def cmdUpdateListbox(self, contacts):

        currentContacts = contacts
        self.contactPairs = {}
        self.contactsList.delete(0,tk.END)
        for x in currentContacts:
            self.contactPairs[len(self.contactPairs)+1] = x
            tmpName = self.contactPairs[len(self.contactPairs)].fname + " " + self.contactPairs[len(self.contactPairs)].lname
            self.contactsList.insert(tk.END,tmpName)
        self.unUpdated = 0

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
        self.contactsList.bind('<<ListboxSelect>>', self.onSelect)

        self.contactPairs = {}

        #add scrollbar to contactsList
        #contactsList.config(yscrollcommand=sbContactsList.set)
        #sbContactsList.config(command=contactsList.yview())

        #############################
        #Entry/entryFrame
        #############################

        #Name
        self.labelName = tk.Label(self.EntryFrame, text="Name")
        self.labelName.grid(row=0,column=0)

        self.entryName = tk.Entry(self.EntryFrame, textvariable=self.svName)
        self.entryName.grid(row=1,column=0)

        #Address line 1
        self.labelAddressLast = tk.Label(self.EntryFrame, text="Last")
        self.labelAddressLast.grid(row=2,column=0)

        self.entryAddressLast = tk.Entry(self.EntryFrame, textvariable=self.svLast)
        self.entryAddressLast.grid(row=3,column=0)

        #Address line 2
        self.labelAddressDelivery = tk.Label(self.EntryFrame, text="Delivery")
        self.labelAddressDelivery.grid(row=4,column=0)

        self.entryAddressDelivery = tk.Entry(self.EntryFrame, textvariable=self.svDelivery)
        self.entryAddressDelivery.grid(row=5,column=0)

        #Address line 3
        self.labelAddressSecond = tk.Label(self.EntryFrame, text="Second")
        self.labelAddressSecond.grid(row=6,column=0)

        self.entryAddressSecond = tk.Entry(self.EntryFrame, textvariable=self.svSecond)
        self.entryAddressSecond.grid(row=7,column=0)

        #Email
        self.labelEmail = tk.Label(self.EntryFrame, text="Email Address")
        self.labelEmail.grid(row=8,column=0)

        self.entryEmail = tk.Entry(self.EntryFrame, textvariable=self.svEmail)
        self.entryEmail.grid(row=9,column=0)

        #Phone
        self.labelPhone = tk.Label(self.EntryFrame, text="Phone Number")
        self.labelPhone.grid(row=10,column=0)

        self.entryPhone = tk.Entry(self.EntryFrame, textvariable=self.svPhone)
        self.entryPhone.grid(row=11,column=0)

        #############################
        #Buttons/buttonFrame
        #############################
        self.btnAddContact = tk.Button(self.buttonFrame, text="Add", command=self.cmdAdd)
        self.btnAddContact.grid(row=3, column=0, sticky=tk.W+tk.E)

        self.btnRemoveContact = tk.Button(self.buttonFrame, text="Remove", command=self.cmdRemove)
        self.btnRemoveContact.grid(row=3, column=1, sticky=tk.W+tk.E)

        self.btnUpdateContact = tk.Button(self.buttonFrame, text="Update", command=self.cmdUpdate)
        self.btnUpdateContact.grid(row=3, column=2, sticky=tk.W+tk.E)

        self.btnSortName = tk.Button(self.buttonFrame, text="Sort, Name", command=self.cmdSortName)
        self.btnSortName.grid(row=3,column=3, sticky=tk.W+tk.E)

        self.btnSortZIP = tk.Button(self.buttonFrame, text="Sort, ZIP", command=self.cmdSortZIP)
        self.btnSortZIP.grid(row=2,column=3, sticky=tk.W+tk.E)

        self.btnClearContact = tk.Button(self.buttonFrame, text="Clear Fields", command=self.cmdClearContact)
        self.btnClearContact.grid(row=1,column=2, sticky=tk.W+tk.E)

        #Search
        self.entrySearch = tk.Entry(self.buttonFrame, width = 25)
        self.entrySearch.grid(row=1,column=0, columnspan=2)

        self.btnSearch = tk.Button(self.buttonFrame, text="Search Name", command=self.cmdNameSearch)
        self.btnSearch.grid(row=2,column=0, sticky=tk.W+tk.E)

        self.btnClear = tk.Button(self.buttonFrame, text="Clear", command=self.cmdClear)
        self.btnClear.grid(row=2,column=1, sticky=tk.W+tk.E)

        self.btnGeneralSearch = tk.Button(self.buttonFrame, text="General Search", command=self.cmdGeneralSearch)
        self.btnGeneralSearch.grid(row=2,column=2, sticky=tk.W+tk.E)

