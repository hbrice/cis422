__author__ = 'lucasr'
from model import addressbook
import os.pat
import pickle

class addressbooks:
    """docstring for addressbooks"""
    def __init__(self):
        self.addressBooks = []

    def addAddressBook(self, addrBook):
        self.addressBooks.append(addrBook)
    
    """Save: Function for saving an addressbooks instance.
    The arguments are a file name, and an overwrite flag. If no flag is passed 
    the default is to not overwrite that file if it exists."""
    def save(self, fileName, overwrite = false):
        if !os.path.exists(fileName) or overwrite:
            output = open(fileName, 'w+')
            pickle.dump(self, output)
            output.close()
        else:
            print "AddressBooks file already exists. Overwrite?"
            
            
