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
import tkMessageBox
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
        contactList = []
        if (len(indices) > 1):
            # This should be printed on the GUI
            # print("More than one contact found:")
            for i in indices:
                contactList.append(self.contacts[i])
            return contactList
        elif (len(indices) == 1):
            contact.append(self.contacts[indices[0]])
            return contactList
        else:
            tkMessageBox.showinfo("Alert", "Contact Not Found!", icon='warning')

    def generalSearchContacts(self, keyword):
        found = []
        for i in self.contacts:
            if keyword.lower() in i:
                found.append(i)
        if (found == []):
            tkMessageBox.showinfo("Alert", "No Matches Found!", icon='warning')
        return found

    def removeContact(self, contact):
        #self.contacts.remove(contact)
        indices = [i for i, val in enumerate(self.contacts) if val == contact]
        for i in indices:
            if (self.contacts[i].firstZip == contact.firstZip):
                self.contacts.pop(i)

    def sortByLname(self):
        lnameSortList = sorted(self.contacts, key=attrgetter('lname'))
        self.contacts = lnameSortList

    def sortByZip(self):
        zipSortList = sorted(self.contacts, key=attrgetter('firstZip'))
        self.contacts = zipSortList

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



