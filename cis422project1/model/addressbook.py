__author__ = 'lucasr'
from model import contact

class addressbook:
    """docstring for addressbook"""
    def __init__(self):
        self.contacts = []

    def addContact(self, contact):
        self.contacts.append(contact)