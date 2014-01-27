from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
from tkFileDialog import asksaveasfilename


class AddressBookFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def cmdAdd(self):
        print "Add contact"

    def cmdRemove(self):
        print "Remove"

    def cmdSearch(self):
        print "Search"

    def cmdUpdate(self):
        print "Update"



    def initUI(self):

        self.parent.title("AddressBooks")

        self.pack(fill=BOTH, expand=1)
        self.var = IntVar()


        #TO-DO add scrollbar, need to make frame to hold listbox and scrollbar then add that frame

        #scrollbar for contactsList
        sbContactsList = Scrollbar(self)
        sbContactsList.pack(side=RIGHT, fill=Y)

        #Contacts list
        contactsList = Listbox(self, width=25, height=15)
        contactsList.pack()
        contactsList.place(x=25, y=100)

        #add scrollbar to contactsList
        contactsList.config(yscrollcommand=sbContactsList.set)
        sbContactsList.config(command=contactsList.yview())

        contactsList.insert(END,"John Smith")
        contactsList.insert(END,"Jane Smith")

        #Contact info

        #Name
        labelName = Label(self, text="Name")
        labelName.pack()
        labelName.place(x=200,y=90)

        entryName = Entry(self)
        entryName.pack()
        entryName.place(x=200,y=110)

        #Address line 1
        labelAddress1 = Label(self, text="Address Line 1")
        labelAddress1.pack()
        labelAddress1.place(x=200,y=140)

        entryAddress1 = Entry(self)
        entryAddress1.pack()
        entryAddress1.place(x=200,y=160)

        #Address line 2
        labelAddress2 = Label(self, text="Address Line 2")
        labelAddress2.pack()
        labelAddress2.place(x=200,y=190)

        entryAddress2 = Entry(self)
        entryAddress2.pack()
        entryAddress2.place(x=200,y=210)


        #Email
        labelEmail = Label(self, text="Email Address")
        labelEmail.pack()
        labelEmail.place(x=200,y=240)

        entryEmail = Entry(self)
        entryEmail.pack()
        entryEmail.place(x=200,y=260)

        #Phone
        labelEmail = Label(self, text="Phone Number")
        labelEmail.pack()
        labelEmail.place(x=200,y=290)

        entryEmail = Entry(self)
        entryEmail.pack()
        entryEmail.place(x=200,y=310)

        #buttons
        btnAddContact = Button(self, text="Add", command=self.cmdAdd)
        btnAddContact.pack(fill=BOTH, expand=1)
        btnAddContact.place(x=25, y=350)

        btnRemoveContact = Button(self, text="Remove", command=self.cmdRemove)
        btnRemoveContact.pack(fill=BOTH, expand=1)
        btnRemoveContact.place(x=67, y=350)

        btnUpdateContact = Button(self, text="Update", command=self.cmdUpdate)
        btnUpdateContact.pack(fill=BOTH, expand=1)
        btnUpdateContact.place(x=130, y=350)


        #Search
        entrySearch = Entry(self, width = 15)
        entrySearch.pack()
        entrySearch.place(x=25,y=392)

        btnSearch = Button(self, text="Search", command=self.cmdSearch)
        btnSearch.pack(fill=BOTH, expand=1)
        btnSearch.place(x=130, y=390)



