__author__ = 'lucasr'
from model import contact

class addressbook:
    """docstring for addressbook"""
    def __init__(self):
        self.contacts = []

    def addContact(self, contact):
        self.contacts.append(contact)

    def removeContact(self, contact):
        self.contacts.remove(contact)

    def displayAllContacts(self):
        for x in range(0, len(self.contacts))
            print self.contacts[x].fname
            print self.contacts[x].lname
            print self.contacts[x].addressList
            print self.contacts[x].emailList
            print self.contacts[x].phoneNumberList
