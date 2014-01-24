__author__ = 'lucasr'
from model.address import address

class contact:
    """docstring for contact"""
    def __init__(self, recipient):
        # Last: City State Zip
        # Delivery: 1401 SW Main St.
        # Second: " " or APT 4
        # Recipient: John Doe
        # Phone: (503) 809-9120
        # addr = address(last, delivery, second)
        self.fname = recipient.lower().split(" ")[0]
        self.lname = recipient.lower().split(" ")[1]
        self.addressList = []
        self.emailList = []
        self.phoneNumberList = []

    def __eq__(self, other):
        return (self.fname == other.fname) and (self.lname == other.lname)

    def __str__(self):
        print(self.fname, " ", self.lname)
        print(self.addressList)
        print(self.emailList)
        print(self.phoneNumberList)

    def __contains__(self, item):
        return (item == self.fname) or (item == self.lname) \
            or (item in self.addressList) or (item in self.emailList) \
            or (item in self.phoneNumberList)

    def addAddresses(self, addr):
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




