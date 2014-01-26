__author__ = 'lucasr'
import os, sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

import addressbook
import contact
import address

def main():
    testAddressBook = addressbook()
    testContact1 = contact("John Doe")
    testLast = "Alameda CA 94501"
    testDelivery = "1401 SW Main St."
    testSecond = "Apt 4"
    testAddr = address(testLast, testDelivery, testSecond)
    testEmail = "jdoe@gmail.com"
    testEmail2 = "doe@uoregon.edu"
    testPhoneNumber = "542-345-6745"
    testContact1.addAddress(testAddr)
    testContact1.addEmail(testEmail)
    testContact1.addEmail(testEmail2)
    testContact1.addPhoneNumber(testPhoneNumber)
    testAddressBook.addContact(testContact1)
    print(testContact1)
    print(testAddressBook)




if __name__ == '__main__':
    main()
