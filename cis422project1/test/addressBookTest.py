__author__ = 'lucasr'
from model.addressbook import addressbook
from model.contact import contact

def main():
    test = addressbook()
    testContact1 = contact("John Doe")

if __name__ == '__main__':
    main()