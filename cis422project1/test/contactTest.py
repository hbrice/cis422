__author__ = 'lucasr'
from model.contact import contact
from model.address import address

def main():
    last = "Trentwood OR 94501"
    delivery = "1402 SW Alder st."
    second = "APT 11"
    testAddress = address(last, delivery, second)
    testRecipient = "John Doe"
    testContact = contact(testRecipient)
    testEmail = "jdoe@gmail.com"
    testEmail2 = "doe@uoregon.edu"
    testPhoneNumber = "542-345-6745"
    testContact.addAddress(testAddress)
    testContact.addEmail(testEmail)
    testContact.addEmail(testEmail2)
    testContact.addPhoneNumber(testPhoneNumber)
    print(testContact)
    testContact.removeAddress(testAddress)
    print(testContact)
if __name__ == '__main__':
    main()