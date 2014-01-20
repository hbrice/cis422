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
        for x in range(0, len(contacts))
            print contacts[x].fname
