__author__ = 'lucasr'

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

from model.addressbook import addressbook
from model.contact import contact
from model.address import address

def main():
    testAddressBook = addressbook()
    testContact1 = contact("John Doe")
    testLast = "Alameda CA 94501"
    testDelivery = "1401 SW Main St."
    testSecond = "Apt 4"
    testAddr = address(testLast, testDelivery, testSecond)
    print(testAddr.last)
    print(testAddr.delivery)
    print(testAddr.second)
    print(testAddr)
    #testContact1.addAddress(testAddr)
    #testContact1.addEmail("jdoe@gmail.com")
    #testContact1.addPhoneNumber("534-235-1356")
    #testAddressBook.addContact(testContact1)
    #print(testAddressBook.contacts)
    #print(testAddressBook)
if __name__ == '__main__':
    main()
