__author__ = 'lucasr'
from model import address, email, phoneNumber

class contact:
    """docstring for contact"""
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.addressList = []
        self.emailList = []
        self.phoneNumberList = []

    def __eq__(self, other):
        return (self.fname == other.fname) and (self.lname == other.lname) \
            and (self.addressList == other.addressList) and (self.emailList == other.emailList) \
            and (self.phoneNumberList == other.phoneNumberList)

    def addAddresses(self, addr):
        self.addressList.append(addr)

    def addEmail(self, email):
        self.emailList.append(email)

    def addPhoneNumber(self, phoneNumber):
        self.phoneNumberList.append(phoneNumber)

    def removeAddress(self, addr):
        try:
            self.addressList.remove(addr)
        except ValueError:
            return -1

    def removeEmail(self, email):
        try:
            self.emailList.remove(email)
        except ValueError:
            return -1

    def removePhoneNumber(self, phoneNumber):
        try:
            self.phoneNumberList.remove(phoneNumber)
        except ValueError:
            return -1




