__author__ = 'lucasr'

import os, sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model'))
if not path in sys.path:
    sys.path.insert(1, path)
del path


import contact
from operator import attrgetter

class addressbook:
    """docstring for addressbook"""
    def __init__(self):
        self.contacts = []

    def __str__(self):
        output = ""
        frame = "+++++++++++++++++++++++++++++++++++++"
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
        else:
            print(self.contacts[indices[0]])

    def generalSearchContacts(self, keyword):
        for i in self.contacts:
            if keyword in i:
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
        print(lnameSortList)

    def sortByZip(self):
        zipSortList = sorted(self.contacts, key=attrgetter('addressList')[0].zip)
        print(zipSortList)

    def export(self, contacts):
        """Export a line for each contact in the list "contacts" using the specified tab seperated list
           Last\tDelivery\tSecond\Recipient\tPhone
        """
        with open("tmp.txt") as f:
            for i in contacts:
                with contacts[i] as contact:
                    f.write(contact.address[0].city + " " + contact.address[0].state + " " + contact.address[0].zip + "\t")
                    f.write(contact.address[0].addressNumber + " " + contact.address[0].address + "\t")
                    f.write("\t")#f.write(contact.address[0].secondLine + "\t")# second line not implemented yet
                    f.write(contact.fname + " " + contact.lname + "\t")
                    f.write("\n")





