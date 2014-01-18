__author__ = 'lucasr'
from model import address, email, phoneNumber

class contact:
    """docstring for contact"""
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.addresses = []
        self.emails = []
        self.phoneNumbers = []

    def addAddresses(self, addr):
        self.addresses.append(addr)

    def addEmail(self, email):
        self.emails.append(email)

    def addPhoneNumber(self, phoneNumber):
        self.phoneNumbers.append(phoneNumber)
