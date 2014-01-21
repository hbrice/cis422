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
        return (self.fname == other.fname) and (self.lname == other.lname)

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
            print("Address not found!")

    def removeEmail(self, email):
        try:
            self.emailList.remove(email)
        except ValueError:
            print("Email not found!")

    def removePhoneNumber(self, phoneNumber):
        try:
            self.phoneNumberList.remove(phoneNumber)
        except ValueError:
            print("Phone Number not found!")




