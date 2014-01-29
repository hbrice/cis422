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


        self.logic = addressBookLogic #run
        #self.logic = addressbook.addressbook #code

        self.initUI()
        self.buttonFrame.pack(side=tk.BOTTOM, pady=5)
        self.contactFrame.pack(side=tk.LEFT)
        self.EntryFrame.pack(side=tk.LEFT, padx=5)
        self.cmdUpdateListbox()
        self.contactPairs

    """function that is bound the the listbox selection"""
    def onSelect(self, evt):
        w = evt.widget
        index = int(w.curselection()[0]) + 1
        tmpContact = self.contactPairs[index]
        self.entryName.delete(0,tk.END)
        self.entryName.insert(0, tmpContact.fname + " " + tmpContact.lname)
        self.entryEmail.delete(0,tk.END)
        self.entryEmail.insert(0, tmpContact.emailList[0])
        self.entryPhone.delete(0,tk.END)
        self.entryPhone.insert(0, tmpContact.phoneNumberList[0])



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
        #self.tempContact = self.logic.findContactByName(self.entryName.get())
        tmpSelection = self.contactsList.curselection()
        tmpIndex = int(tmpSelection[0])
        tmpIndex=tmpIndex+1
        print tmpIndex
        if len(tmpSelection) > 1:
            tkMessageBox.showinfo("Too Many!", "Too many entries selected!")
        else:
            tempContact = self.contactPairs[tmpIndex]
            print tempContact

    def cmdClear(self):
        print "Clear"

    def cmdSortName(self):
        print "sort by name"

    def cmdSortZIP(self):
        print "sort by ZIP"

    def cmdUpdateListbox(self):
        self.currentContacts = self.logic.contacts
        for x in self.currentContacts:
            self.contactPairs[len(self.contactPairs)+1] = x
            tmpName = self.contactPairs[len(self.contactPairs)].fname + " " + self.contactPairs[len(self.contactPairs)].lname
            self.contactsList.insert(tk.END,tmpName)



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

        self.btnSortName = tk.Button(self.buttonFrame, text="Sort, Name", command=self.cmdSortName)
        self.btnSortName.grid(row=0,column=5, sticky=tk.W+tk.E)

        self.btnSortZIP = tk.Button(self.buttonFrame, text="Sort, ZIP", command=self.cmdSortZIP)
        self.btnSortZIP.grid(row=1,column=5, sticky=tk.W+tk.E)


        #Search
        self.entrySearch = tk.Entry(self.buttonFrame, width = 15)
        self.entrySearch.grid(row=1,column=0)

        self.btnSearch = tk.Button(self.buttonFrame, text="Search", command=self.cmdSearch)
        self.btnSearch.grid(row=1,column=1, sticky=tk.W+tk.E)

        self.btnClear = tk.Button(self.buttonFrame, text="Clear", command=self.cmdClear)
        self.btnClear.grid(row=1,column=2, sticky=tk.W+tk.E)




