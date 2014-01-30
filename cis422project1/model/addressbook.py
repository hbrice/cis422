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
import pickle
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
            contactList.append(self.contacts[indices[0]])
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
            if (self.contacts[i].cid == contact.cid):
                self.contacts.pop(i)

    def mergeAddressBook(self, otherAddressBook):
        for i in otherAddressBook.contacts:
            self.addContact(i)

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
        if os.path.exists(fileName) == 0:
            f = open(fileName, 'w')
            f.close

        with open(fileName, 'w') as f:
            f.write("Last\tDelivery\tSecond\tRecipient\tPhone\tEmail\n")
            for i in range(0,len(contacts)):
                    if len(contacts[i].addressList) > 0:
                        f.write(contacts[i].addressList[0].city + " " + contacts[i].addressList[0].state + " " + contacts[i].addressList[0].zip + "\t")
                        f.write(contacts[i].addressList[0].addressNumber + " " + contacts[i].addressList[0].address + "\t")
                        f.write(contacts[i].addressList[0].second + "\t")
                    else:
                        f.write("\t\t\t")
                    f.write(contacts[i].fname + " " + contacts[i].lname + "\t")
                    if len(contacts[i].phoneNumberList) > 0:
                        f.write(contacts[i].phoneNumberList[0] + "\t")
                    else:
                        f.write("\t")
                    if len(contacts[i].emailList) > 0:
                        f.write(contacts[i].emailList[0])
                    else:
                        f.write("\t")
                    f.write("\n")
        f.close
    
    #takes a fileName and uses the parser, contact, and address to add each line of the file to the addressbook.
    def addressBookImport(self, fileName, app):
        if os.path.exists(fileName):
            f = open(fileName, 'r')
            data = utils.importParse(f)
            for element in data:
                print element
                newContact = contact(element['Recipient'])
                newAddress = address(element['Last'], element['Delivery'], element['Second'])
                newContact.addAddress(newAddress)
                if 'Phone' in element:
                    newContact.addPhoneNumber(element['Phone'])
                if 'Email' in element:
                    newContact.addEmail(element['Email'])
                self.addContact(newContact)
                app.cmdUpdateListbox(self.contacts)
        #todo: error reporting
        print "Path doesn't exist."

    """Save: Function for saving an addressbooks instance.
    The arguments are a file name, and an overwrite flag. If no flag is passed
    the default is to not overwrite that file if it exists."""
    def save(self, fileName, overwrite = False):
        if not os.path.exists(fileName) or overwrite:
            output = open(fileName, 'w+')
            pickle.dump(self, output)
            output.close()
        else:
            print("AddressBooks file already exists. Overwrite?")

    """Load: sets the addressBooksList of self to the unpickled's list."""
    def load(self, fileName):
        if os.path.exists(fileName):
             input = open(fileName, 'rb')
             data = pickle.load(fileName)
             if type(data) is self.addressBooksList:
             	self.addressBooksList = data.addressBooksList

