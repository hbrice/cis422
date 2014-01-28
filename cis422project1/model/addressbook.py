__author__ = 'lucasr'

import os, sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model'))
if not path in sys.path:
    sys.path.insert(1, path)
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../controller'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

import utils
from contact import contact
from address import address
from operator import attrgetter

class addressbook:
    """docstring for addressbook"""
    def __init__(self):
        self.contacts = []

    def __str__(self):
        output = ""
        frame = "+++++++++++++++++++++++++++++++++++++\n"
        for i in self.contacts:
            output = output + frame
            output = output + str(i)
        return output

    def addContact(self, contact):
        self.contacts.append(contact)

    def findContactByName(self, recipient):
        tmp = contact(recipient)
        indices = [i for i, val in enumerate(self.contacts) if val == tmp]
        if (len(indices) > 1):
             print("More than one contact found:")
             for i in indices:
                print(i, " ", self.contacts[indices[i]])
        elif (len(indices) == 1):
            print(self.contacts[indices[0]])
        else:
            print("Contact Not Found!")

    def generalSearchContacts(self, keyword):
        for i in self.contacts:
            if keyword.lower() in i:
                print(i)

    def removeContactByName(self, recipient):
        tmp = contact(recipient)
        indices = [i for i, val in enumerate(self.contacts) if val == tmp]
        if (len(indices) > 1):
            print("More than one contact found:")
            for i in indices:
                print(i, " ", self.contacts[indices[i]])
            idx = input("Please specify by index for the correct contact to delete. "
                        "Or type 'all' to delete all contacts found: ")
            if idx != "all":
                try:
                    del self.contacts[idx]
                except ValueError:
                    print("Not a correct index!")
            else:
                for i in indices:
                    del self.contacts[indices[i]]
        else:
            del self.contacts[indices[0]]

    def sortByLname(self):
        lnameSortList = sorted(self.contacts, key=attrgetter('lname'))
        self.contacts = lnameSortList
        #print(lnameSortList)

    def sortByZip(self):
        #zipList = [int(x.firstZip) for x in self.contacts]
        zipSortList = sorted(self.contacts, key=attrgetter('firstZip'))
        self.contacts = zipSortList
        #print(zipSortList)

    def export(self, contacts, fileName):
        """Export a line for each contact in the list "contacts" using the specified tab seperated list
           Last\tDelivery\tSecond\Recipient\tPhone
        """
        with open(fileName) as f:
            for i in contacts:
                with contacts[i] as contact:
                    f.write(contact.address[0].city + " " + contact.address[0].state + " " + contact.address[0].zip + "\t")
                    f.write(contact.address[0].addressNumber + " " + contact.address[0].address + "\t")
                    f.write("\t")#f.write(contact.address[0].secondLine + "\t")# second line not implemented yet
                    f.write(contact.fname + " " + contact.lname + "\t")
                    f.write("\n")
    
    #takes a fileName and uses the parser, contact, and address to add each line of the file to the addressbook.
    def addressBookImport(self, fileName, contactList):
        if os.path.exists(fileName):
            f = open(fileName, 'r')
            data = utils.importParse(fileName)
            for element in data:
                newContact = contact(element['recipient'])
                newAddress = address(element['last'], element['delivery'], element['second'])
                newContact.addAddress(newAddress)
                self.addContact(newContact)
                contactList.insert(0,element['recipient'])
        #todo: error reporting
        print "Path doesn't exist."



