__author__ = 'lucasr'
from model import addressbook

class addressbooks:
    """docstring for addressbooks"""
    def __init__(self):
        self.addressBooks = []

    def addAddressBook(self, addrBook):
        self.addressBooks.append(addrBook)