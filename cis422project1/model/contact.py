__author__ = 'lucasr'
from model import address

class contact:
    """docstring for contact"""
    def __init__(self, recipient):
        # Last: City State Zip
        # Delivery: 1401 SW Main St.
        # Second: " " or APT 4
        # Recipient: John Doe
        # Phone 503 809-9120
        # DO CONTACTS NEED ADDRESS
        # addr = address(last, delivery, second)
        self.recipient = recipient
        self.addressList = []
        self.emailList = []
        self.phoneNumberList = []

    def __eq__(self, other):
        return (self.recipient.lower() == other.recipient.lower())

    def __str__(self):
        print(self.recipient)
        print(self.addressList)
        print(self.emailList)
        print(self.phoneNumberList)

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




