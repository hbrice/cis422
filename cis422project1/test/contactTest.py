__author__ = 'lucasr'

import os, sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

from address import address
from contact import contact

def main():
    last = "Trentwood OR 94701"
    delivery = "1402 SW Alder st."
    second = "APT 11"
    testAddress = address(last, delivery, second)
    testRecipient = "John Doe"

    last2 = "Oakland CA 94501"
    delivery2 = "1244 Broadway st."
    second2 = "APT 11"
    testAddress2 = address(last2, delivery2, second2)
    testRecipient2 = "Lucas Rondenet"

    testContact = contact(testRecipient)
    testContact2 = contact(testRecipient2)

    testEmail = "jdoe@gmail.com"
    testEmail2 = "doe@uoregon.edu"
    testPhoneNumber = "542-345-6745"
    testEmail3 = "lrondenet@gmail.com"
    testEmail4 = "lucasr@uoregon.edu"
    testPhoneNumber2 = "545-565-7889"

    testContact.addAddress(testAddress)
    testContact.addEmail(testEmail)
    testContact.addEmail(testEmail2)
    testContact.addPhoneNumber(testPhoneNumber)
    testContact2.addAddress(testAddress2)
    testContact2.addEmail(testEmail3)
    testContact2.addEmail(testEmail4)
    testContact2.addPhoneNumber(testPhoneNumber2)

    print(testContact)
    #testContact.removeAddress(testAddress)
    print(testContact)
    print
    print(testContact2)

    testContact.addField("age", "32")
    testContact3 = contact("John Newhall")
    print(testContact.age)
    print(vars(testContact))
    print(vars(testContact2))
    print(vars(testContact3))


if __name__ == '__main__':
    main()
