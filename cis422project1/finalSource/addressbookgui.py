import Tkinter as tk
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
from tkFileDialog import asksaveasfilename
import addressbook
import contact
import address
import tkMessageBox

"""AddressBookFrame represents the internal frame within an address book, it ties together the addressbook backend and the GUI"""
class AddressBookFrame():

    def __init__(self, master, addressBookLogic):

        """these variables will be used to monitor states for both the entry boxes and the addressbook
        to make sure information dosen't get lost without the user knowing"""
        self.unSavedChanges = 0
        self.unUpdated = 0

        """these variables will be bound to the entry boxes """
        self.svName = tk.StringVar()
        self.svLast = tk.StringVar()
        self.svDelivery = tk.StringVar()
        self.svSecond = tk.StringVar()
        self.svEmail = tk.StringVar()
        self.svPhone = tk.StringVar()

        """set traces for each entryboxe variable and the action event is to call entryChanged"""
        self.svName.trace("w", self.entryChanged)
        self.svLast.trace("w", self.entryChanged)
        self.svDelivery.trace("w", self.entryChanged)
        self.svSecond.trace("w", self.entryChanged)
        self.svEmail.trace("w", self.entryChanged)
        self.svPhone.trace("w", self.entryChanged)

        """keep a record of the calling object"""
        self.master = master

        """setup the outermost frame (frame container) & add draw it to master, this will hold the three internal frames"""
        self.frame = tk.Frame(self.master)
        self.frame.grid(row=0,column=0)

        """add the three sub frames to the frame container"""
        self.contactFrame = tk.Frame(self.frame)
        self.EntryFrame = tk.Frame(self.frame)
        self.buttonFrame = tk.Frame(self.frame)

        """internal referance to the addressbook object"""
        self.logic = addressBookLogic #run

        """setup all the widgets on the frames"""
        self.initUI()

        """arrange & draw the three frames"""
        self.buttonFrame.pack(side=tk.BOTTOM, pady=5)
        self.contactFrame.pack(side=tk.LEFT)
        self.EntryFrame.pack(side=tk.LEFT, padx=5)

        """lastly, update the listbox of contacts"""
        self.cmdUpdateListbox(self.logic.contacts)

    """check for unsaved changes to a selected contact, prombt to user is they're sure, return response"""
    def checkUpdated(self):
        if self.unUpdated == 1:
            result = tkMessageBox.askquestion("Unsaved","You have unsaved changes for the selected contact, are you sure you want to continue?")
            if result == 'no':
                return 0
            else:
                return 1
                self.unUpdated = 0
        return 1

    """anytime a entrybox is changed, set the state for unUpdated"""
    def entryChanged(self, *args):
        self.unUpdated = 1

    """function that is bound the the listbox selection"""
    def onSelect(self, evt):
        """if the user dosen't want to lose unsaved changes, don't continue"""
        if self.checkUpdated() == 0:
            return

        """get the widget that triggered the event"""
        w = evt.widget

        """if there's no contacts in the list don't try & just return"""
        if len(w.curselection()) <= 0:
            return

        """get the selected item and add one"""
        index = int(w.curselection()[0]) + 1
        """get the contact object from the name-value pair"""
        tmpContact = self.contactPairs[index]

        """clear and update all of the contact entryboxes with the selected object information"""
        self.entryName.delete(0,tk.END)
        self.entryName.insert(0, tmpContact.fname + " " + tmpContact.lname)

        self.entryAddressLast.delete(0,tk.END)
        self.entryAddressLast.insert(0, tmpContact.addressList[0].last)

        self.entryAddressDelivery.delete(0,tk.END)
        self.entryAddressDelivery.insert(0, tmpContact.addressList[0].delivery)

        self.entryAddressSecond.delete(0,tk.END)
        self.entryAddressSecond.insert(0, tmpContact.addressList[0].second)

        self.entryEmail.delete(0,tk.END)
        """if there's an email, add it"""
        if len(tmpContact.emailList) > 0:
            self.entryEmail.insert(0, tmpContact.emailList[0])

        self.entryPhone.delete(0,tk.END)
        """if there's a phone number, add it"""
        if len(tmpContact.phoneNumberList) > 0:
            self.entryPhone.insert(0, tmpContact.phoneNumberList[0])
        """set the state to no unUpdated changes"""
        self.unUpdated = 0


    def cmdAdd(self):
        """create a new contact based on the contact's name"""
        self.tempContact = contact.contact(self.entryName.get())
        """build a temp address"""
        self.tempAddress = address.address(self.entryAddressLast.get(),self.entryAddressDelivery.get(),self.entryAddressSecond.get())
        """add the address to the contact object"""
        self.tempContact.addAddress(self.tempAddress)
        """add the email address to the contact object"""
        self.tempContact.addEmail(self.entryEmail.get())
        """get and add the phone number to the contact object"""
        self.tempContact.addPhoneNumber(self.entryPhone.get())
        """add the contact to the address book"""
        self.logic.addContact(self.tempContact)
        """update the listbox"""
        self.cmdUpdateListbox(self.logic.contacts)

        """set the addressbook state to unsaved"""
        self.unSavedChanges = 1

    """function called when the remove button is clicked"""
    def cmdRemove(self):
        """get the current selection"""
        tmpSelection = self.contactsList.curselection()
        """if there's at least one contact selected"""
        if len(tmpSelection) > 0:
            tmpIndex = int(tmpSelection[0])
            tmpIndex=tmpIndex+1
            """if more than once contact is selected display error"""
            if len(tmpSelection) > 1:
                tkMessageBox.showinfo("Too Many!", "Too many entries selected, please remove one at a time.")
            else:
                """get the contact from the name-value pairs"""
                tempContact = self.contactPairs[tmpIndex]
                """remove the contact"""
                self.logic.removeContact(tempContact)

                """clear all the entry boxes"""
                self.entryAddressSecond.delete(0,tk.END)
                self.entryAddressDelivery.delete(0,tk.END)
                self.entryAddressLast.delete(0,tk.END)
                self.entryEmail.delete(0,tk.END)
                self.entryPhone.delete(0,tk.END)
                self.entryName.delete(0,tk.END)
                self.cmdUpdateListbox(self.logic.contacts)
                self.unSavedChanges = 1
        else:
            """if no contacts selected"""
            tkMessageBox.showinfo("Not enough!", "No entries selected.")

    def cmdNameSearch(self):
        """if the user dosen't want to lose unsaved changes, don't continue"""
        if self.checkUpdated() == 0:
            return
        """store the query"""
        query = self.entrySearch.get()
        """if it's not blank, call the address book which will return a contacts list"""
        if query != "":
            results=self.logic.findContactByName(query)
            """if there's results"""
            if results != []:
                """update with the returned results"""
                self.cmdUpdateListbox(results)
            else:
                """else display nothing"""
                self.cmdClearListBox


    def cmdGeneralSearch(self):
        """if the user dosen't want to lose unsaved changes, don't continue"""
        if self.checkUpdated() == 0:
            return
        """store the query"""
        query = self.entrySearch.get()
        """if it's not blank, call the address book which will return a contacts list"""
        if query != "":
            results=self.logic.generalSearchContacts(query)
            """if there's results"""
            if results != []:
                """update with the returned results"""
                self.cmdUpdateListbox(results)
            else:
                """else display nothing"""
                self.cmdClearListBox

    """update a contact"""
    def cmdUpdate(self):
        """get the selection and verify there's 1 selected"""
        tmpSelection = self.contactsList.curselection()
        if len(tmpSelection) > 0:
            """make sure there's just one selected"""
            tmpIndex = int(tmpSelection[0])
            tmpIndex=tmpIndex+1
            if len(tmpSelection) > 1:
                tkMessageBox.showinfo("Too Many!", "Too many entries selected, please update one at a time.")
            else:
                """save the contact"""
                tempContact = self.contactPairs[tmpIndex]
                """remove the contact"""
                self.logic.removeContact(tempContact)
                """add the contact back in with the updated info"""
                self.cmdAdd()
                """addressbook is now unsaved"""
                self.unSavedChanges = 1
        else:
            tkMessageBox.showinfo("Not enough!", "No entries selected.")

    """cmd to clear search results"""
    def cmdClear(self):
        """if the user dosen't want to lose unsaved changes, don't continue"""
        if self.checkUpdated() == 0:
            return
        """clear the search box"""
        self.entrySearch.delete(0,tk.END)
        """update the listbox with the full list of contacts"""
        self.cmdUpdateListbox(self.logic.contacts)

    """clear the entry boxes in preperation to add a new contact"""
    def cmdClearContact(self):
        """if the user dosen't want to lose unsaved changes, don't continue"""
        if self.checkUpdated() == 0:
            return

        """clear all the entry boxes"""
        self.entryAddressSecond.delete(0,tk.END)
        self.entryAddressDelivery.delete(0,tk.END)
        self.entryAddressLast.delete(0,tk.END)
        self.entryEmail.delete(0,tk.END)
        self.entryPhone.delete(0,tk.END)
        self.entryName.delete(0,tk.END)

    """call the addressbook sortByName and update GUI"""
    def cmdSortName(self):
        """if the user dosen't want to lose unsaved changes, don't continue"""
        if self.checkUpdated() == 0:
            return
        """sort by last name"""
        self.logic.sortByLname()
        """update the listbox"""
        self.cmdUpdateListbox(self.logic.contacts)

    """calls the addressbook sortByZip and updates GUI"""
    def cmdSortZIP(self):
        """if the user dosen't want to lose unsaved changes, don't continue"""
        if self.checkUpdated() == 0:
            return
        """sort by zip"""
        self.logic.sortByZip()
        """update the listbox"""
        self.cmdUpdateListbox(self.logic.contacts)

    """empty all items in the listbox"""
    def cmdClearListBox(self):
        """if the user dosen't want to lose unsaved changes, don't continue"""
        if self.checkUpdated() == 0:
            return
        """clear the listbox"""
        self.contactsList.delete(0,tk.END)

    """refresh the contactListBox"""
    def cmdUpdateListbox(self, contacts):
        currentContacts = contacts
        """clear the name-value pairs and the listbox"""
        self.contactPairs = {}
        self.contactsList.delete(0,tk.END)
        """try to itterate through currentConacts, if no contacts just clear the listbox"""
        try:
            for x in currentContacts:
                """add a contact to the name-value pair"""
                self.contactPairs[len(self.contactPairs)+1] = x
                """build the name for display"""
                tmpName = self.contactPairs[len(self.contactPairs)].fname + " " + self.contactPairs[len(self.contactPairs)].lname
                """insert the contact to the listbox"""
                self.contactsList.insert(tk.END,tmpName)
        except TypeError:
            """empty the listbox"""
            self.contactsList.delete(0,tk.END)

        """set unUpdated to 0"""
        self.unUpdated = 0


    """draw all the widgets in the correct place on their frames"""
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

