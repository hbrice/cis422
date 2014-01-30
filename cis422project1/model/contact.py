__author__ = 'lucasr'

import os, sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

from address import address
import tkMessageBox
import uuid
import re

class contact:

    def __init__(self, recipient):
        """
        Takes in recipient field, a name comprised of a first name and last name. Will set all other
        fields initialized but empty:
        addressList, a list of addresses
        firstZip, a int used to sort based on zip of first address
        emailList, a list of emails for contact
        phoneNumberList, a list of phone numbers for contact
        cid, a unique identifier used to distinguish between cases of two contacts with similar attributes (same name)
        """
        # Last: City State Zip
        # Delivery: 1401 SW Main St.
        # Second: " " or APT 4
        # Recipient: John Doe
        # Phone: (503) 809-9120
        # addr = address(last, delivery, second)
        name = recipient.lower().split(" ")
        result = self.checkName(name)
        if (result == True):
            self.fname = name[0]
            self.lname = ' '.join(name[1:])
        else:
            self.fname = ' '.join(name[0:2])
            self.lname = ' '.join(name[2:])
        self.addressList = []
        self.firstZip = 0
        self.emailList = []
        self.phoneNumberList = []
        self.cid = uuid.uuid1()

    def addField(self, name, value):
        """
        Allows for a user to add their own attribute to a contact with a specified value. A user could add an "age"
        attribute by calling contact.addField("age", 21). Only adds to this instance of the contact however and not
        every instance
        """
        # create local fget and fset functions
        get = lambda self: self.getField(name)
        set = lambda self, value: self.setField(name, value)

        # add property to self
        setattr(self.__class__, name, property(get, set))
        # add corresponding local variable
        setattr(self, name, value)

    def setField(self, name, value):
        """
        Helper function used for addField() function. See function for details
        """
        setattr(self, name, value)

    def getField(self, name):
        """
        Helper function used for addField() function. See function for details
        """
        return getattr(self, name)

    def __eq__(self, other):
        """
        Equality function for contacts only compares first name and last name of contact so search
        functionality by full name returns all contacts that have the same first name and last name
        """
        return (self.fname == other.fname) and (self.lname == other.lname)

    def __str__(self):
        """
        Print function used for testing
        prints fname<space>lname<newline>addressList<newline>emailList<newline>phoneNumberList<newLine>
        """
        name = self.fname + " " + self.lname
        tmp = ""
        for i in self.addressList:
            tmp = tmp + str(i)
        emails = ', '.join(self.emailList)
        phoneNumbers = ', '.join(self.phoneNumberList)
        output = name + "\n" + tmp + "\n" + emails + "\n" + phoneNumbers + "\n"
        return output

    def mailingFormat(self):
        # receiepent
        # streetnumber name
        # Apt4 city state zip
        name = self.fname + " " + self.lname
        street = self.addressList[0].addressNumber + " " + self.addressList[0].address
        if (self.addressList[0].last != ""):
            last = self.addressList[0].last + " " + self.addressList[0].city + " " + self.addressList[0].zip
        else:
            last = self.addressList[0].city + " " + self.addressList[0].zip
        output = name + "\n" + street + "\n" + last + "\n"
        return output

    def __repr__(self):
        """
        Print function used for testing
        prints fname<space>lname<newline>addressList<newline>emailList<newline>phoneNumberList<newLine>
        """
        name = self.fname + " " + self.lname
        tmp = ""
        for i in self.addressList:
            tmp = tmp + str(i)
        emails = ', '.join(self.emailList)
        phoneNumbers = ', '.join(self.phoneNumberList)
        output = name + "\n" + tmp + "\n" + emails + "\n" + phoneNumbers + "\n"
        return output

    def __contains__(self, item):
        """
        Finds if item is a substring in any of the fields within a contact. Will check name, addresses, emails, phones
        For example, can find all phone numbers with (510) area codes in this contact
        """
        inName = ((item in self.fname) or (item in self.lname))
        inAddrList = False
        inEmailList = False
        inPhoneList = False
        for i in self.addressList:
            if (item in i):
                inAddrList = True
        for i in self.emailList:
            if (item in i):
                inEmailList = True
        for i in self.phoneNumberList:
            if (item in i):
                inPhoneList = True
        return (inName or inAddrList or inEmailList or inPhoneList)

    def checkName(self, name):
        """
        Makes sure that if name with three words are specified with the correct first name and last name.
        An alert window will pop open an ask if the first name is a two word name or first word name
        Example: Ann Marie Smith, first name could be both Ann Marie or Ann.
        """
        if (len(name) > 2):
            result = tkMessageBox.askquestion("Alert", "We noticed that you have entered in a three word name: " + name +
                                                       ", Is the first word the first name?")
            if (result == 'yes'):
                return True
            else:
                return False
        else:
            return True

    def checkPhone(self, number):
        """
        Makes sure that the phone number has only 10 digits. Does not support phone numbers that have 1 before area code.
        For example: 1 (510) 332 4565 IS NOT SUPPORTED!
        """
        nums = ''.join(x for x in number if x.isdigit())
        if (len(nums) == 10):
            return True
        else: return False

    def checkZip(self, zip):
        """
        Makes sure that the zip is actually a digit and not some random string with chars and numbers
        """
        if(zip.isdigit()):
            return True
        else: return False

    def addAddress(self, addr):
        """
        Adds address to addressList, before adding though makes sure that address is not already there, also
        checks if the zip is correct and adds to firstZip if it is the first address added to the contact (firstZip is
        used to sort all contacts by zip). Alert boxes pop up if the zip is not an integer or if address is already
        added to the contact.
        """
        if (addr not in self.addressList):
            if(self.checkZip(addr.zip)):
                if (self.addressList == []):
                    self.firstZip = int(addr.zip)
                self.addressList.append(addr)
            else:
                tkMessageBox.showinfo("Alert", "Zip is not an Integer!", icon='warning')
        else:
            tkMessageBox.showinfo("Alert", "Address Already Added to This Contacts!", icon='warning')

    def addEmail(self, email):
        """
        Adds email to contact, makes sure its in lower case and not added to contact already. If email is there already

        """
        if (email.lower() not in self.emailList):
            self.emailList.append(email)
        else:
            tkMessageBox.showinfo("Alert", "Email Already added to this contact", icon='warning')

    def addPhoneNumber(self, phoneNumber):
        if(self.checkPhone(phoneNumber)):
            if (phoneNumber not in self.phoneNumberList):
                self.phoneNumberList.append(phoneNumber)
            else:
                tkMessageBox.showinfo("Alert", "Phone number already added to this contact", icon='warning')
        else:
            tkMessageBox.showinfo("Alert", "Phone number is not valid", icon='warning')

    def removeAddress(self, addr):
        try:
            self.addressList.remove(addr)
        except ValueError:
            tkMessageBox.showinfo("Alert", "Address not found!", icon='warning')

    def removeEmail(self, email):
        try:
            self.emailList.remove(email)
        except ValueError:
            tkMessageBox.showinfo("Alert", "Email not found!", icon='warning')

    def removePhoneNumber(self, phoneNumber):
        try:
            self.phoneNumberList.remove(phoneNumber)
        except ValueError:
            tkMessageBox.showinfo("Alert", "Phone Number not found!", icon='warning')
