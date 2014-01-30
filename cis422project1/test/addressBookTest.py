__author__ = 'lucasr'
import os, sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

from addressbook import addressbook
from contact import contact
from address import address

def main():
    testAddressBook = addressbook()

    testContact1 = contact("John Doe")
    testLast1 = "Alameda CA"
    testDelivery1 = "1401 SW Main St."
    testSecond1 = "Apt 4"
    testAddr1 = address(testLast1, testDelivery1, testSecond1)
    testEmail1 = "jdoe@gmail.com"
    testEmail2 = "doe@uoregon.edu"
    testPhoneNumber1 = "542-345-6745"
    testContact1.addAddress(testAddr1)
    testContact1.addEmail(testEmail1)
    testContact1.addEmail(testEmail2)
    testContact1.addPhoneNumber(testPhoneNumber1)
    #print(testContact1)

    '''testContact2 = contact("Mary Sue")
    testLast2 = "Venice CA 97979"
    testDelivery2 = "56 Trent St."
    testSecond2 = ""
    testAddr2 = address(testLast2, testDelivery2, testSecond2)
    testEmail2_1 = "marys@gmail.com"
    testEmail2_2 = "msue@uoregon.edu"
    testPhoneNumber2 = "542-524-5820"
    testContact2.addAddress(testAddr2)
    testContact2.addEmail(testEmail2_1)
    testContact2.addEmail(testEmail2_2)
    testContact2.addPhoneNumber(testPhoneNumber2)

    testContact3 = contact("Eddy Adams")
    testLast3 = "Oakland CA 94505"
    testDelivery3 = "345 Alder St."
    testSecond3 = ""
    testAddr3 = address(testLast3, testDelivery3, testSecond3)
    testEmail3_1 = "erodgers@gmail.com"
    testEmail3_2 = "reddy@uoregon.edu"
    testPhoneNumber3 = "233-595-9090"
    testContact3.addAddress(testAddr3)
    testContact3.addEmail(testEmail3_1)
    testContact3.addEmail(testEmail3_2)
    testContact3.addPhoneNumber(testPhoneNumber3)

    testContact4 = contact("John Evan")
    testLast4 = "Hollywood CA 97801"
    testDelivery4 = "1401 Xavier St."
    testSecond4 = "Apt 14"
    testAddr4 = address(testLast4, testDelivery4, testSecond4)
    testEmail4_1 = "johndoe@gmail.com"
    testEmail4_2 = "doe05@uoregon.edu"
    testPhoneNumber4 = "542-444-8967"
    testContact4.addAddress(testAddr4)
    testContact4.addEmail(testEmail4_1)
    testContact4.addEmail(testEmail4_2)
    testContact4.addPhoneNumber(testPhoneNumber4)

    testAddressBook.addContact(testContact1)
    testAddressBook.addContact(testContact2)
    testAddressBook.addContact(testContact3)
    testAddressBook.addContact(testContact4)

    #testAddrBooks = addressbooks()
    #testAddrBooks.addAddressBook(testAddressBook)

    testContact5 = contact("George Simon")
    testLast5 = "Eugene OR 94701"
    testDelivery5 = "1401 SW Main St."
    testSecond5 = "Apt 6"
    testAddr5 = address(testLast5, testDelivery5, testSecond5)
    testEmail5_1 = "simon@gmail.com"
    testEmail5_2 = "gsimon@uoregon.edu"
    testPhoneNumber5 = "542-111-2345"
    testContact5.addAddress(testAddr5)
    testContact5.addEmail(testEmail5_1)
    testContact5.addEmail(testEmail5_2)
    testContact5.addPhoneNumber(testPhoneNumber5)

    testContact6 = contact("Ben Foreman")
    testLast6 = "Tempei WA 94401"
    testDelivery6 = "1403 West St."
    testSecond6 = ""
    testAddr6 = address(testLast6, testDelivery6, testSecond6)
    testEmail6_1 = "bforeman@gmail.com"
    testEmail6_2 = "benf@uoregon.edu"
    testPhoneNumber6 = "542-322-1901"
    testContact6.addAddress(testAddr6)
    testContact6.addEmail(testEmail6_1)
    testContact6.addEmail(testEmail6_2)
    testContact6.addPhoneNumber(testPhoneNumber6)

    print(testContact5)
    print(testContact6)

    testAddressBook2 = addressbook()
    testAddressBook2.addContact(testContact5)
    testAddressBook2.addContact(testContact6)
    testAddressBook.mergeAddressBook(testAddressBook2)

    print(testAddressBook)



    #testAddressBook.generalSearchContacts(".edu")
    #print(testContact1)
    #print(testAddressBook)
    #testAddressBook.sortByLname()
    #print(testAddressBook)
    #print("+++++++++++++++++++++++++++++++++++++")
    #tmp = testAddressBook.findContactByName("John Doe")
    #print(tmp)
    #print(testContact1 == testContact4)
    #testAddressBook.removeContact(testContact1)
    #print(testAddressBook)
    #print(testContact1.cid == testContact3.cid)
    #print(testContact4.cid)
    #tmp2 = testAddressBook.generalSearchContacts("John")
    #print(tmp2)
    #testAddressBook.removeContactByName("John Doe")
    #testAddressBook.sortByZip()
    #print(testAddressBook)
    #print("***************")
    #print(testContact1.firstZip)
    #print(testContact2.firstZip)
    #print(testContact3.firstZip)
    #
    #testAddressBook.findContactByName("Je")
    # testAddressBook.generalSearchContacts("SW2")
    # THIS WORKS!!
    #testAddressBook.removeContactByName("John Doe")
    #print(testAddressBook)'''

if __name__ == '__main__':
    main()
