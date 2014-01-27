__author__ = 'lucasr'

import os, sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

from address import address

class contact:
    """docstring for contact"""
    def __init__(self, recipient):
        # Last: City State Zip
        # Delivery: 1401 SW Main St.
        # Second: " " or APT 4
        # Recipient: John Doe
        # Phone: (503) 809-9120
        # addr = address(last, delivery, second)
        name = recipient.lower().split(" ")
        self.fname = name[0]
        self.lname = ' '.join(name[1:])
        self.addressList = []
        self.emailList = []
        self.phoneNumberList = []

    def addField(self, name, value):
        # create local fget and fset functions
        get = lambda self: self.getField(name)
        set = lambda self, value: self.setField(name, value)

        # add property to self
        setattr(self.__class__, name, property(get, set))
        # add corresponding local variable
        setattr(self, name, value)

    def setField(self, name, value):
        setattr(self, name, value)

    def getField(self, name):
        return getattr(self, name)

    def __eq__(self, other):
        return (self.fname == other.fname) and (self.lname == other.lname)

    def __str__(self):
        name = self.fname + " " + self.lname
        tmp = ""
        for i in self.addressList:
            tmp = tmp + str(i)
        emails = ', '.join(self.emailList)
        phoneNumbers = ', '.join(self.phoneNumberList)
        output = name + "\n" + tmp + "\n" + emails + "\n" + phoneNumbers
        return output

    def __contains__(self, item):
        return (item == self.fname) or (item == self.lname) \
            or (item in self.addressList) or (item in self.emailList) \
            or (item in self.phoneNumberList)

    def addAddress(self, addr):
        if (addr not in self.addressList):
            self.addressList.append(addr)
        else:
            print("Address already added to this contact")

    def addEmail(self, email):
        if (email.lower() not in self.emailList):
            self.emailList.append(email)
        else:
            print("Email already added to this contact")

    def addPhoneNumber(self, phoneNumber):
        if (phoneNumber not in self.phoneNumberList):
            self.phoneNumberList.append(phoneNumber)
        else:
            print("Phone number already added to this contact")

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




