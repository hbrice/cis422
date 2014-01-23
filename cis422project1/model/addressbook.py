__author__ = 'lucasr'
from model import contact

class addressbook:
    """docstring for addressbook"""
    def __init__(self):
        self.contacts = []

    def addContact(self, contact):
        self.contacts.append(contact)

    def removeContact(self, contact):
        self.contacts.remove(contact)

    def displayAllContacts(self):
        for x in range(0, len(self.contacts)):
            print(self.contacts[x].fname)
            print(self.contacts[x].lname)
            print(self.contacts[x].addressList)
            print(self.contacts[x].emailList)
            print(self.contacts[x].phoneNumberList)

    def export(self, contacts):
        """Export a line for each contact in the list "contacts" using the specified tab seperated list
           Last\tDelivery\tSecond\Recipient\tPhone
        """
        with open("tmp.txt") as f:
            for i in contacts:
                with contacts[i] as contact:
                    f.write(contact.address[0].city + " " + contact.address[0].state + " " + contact.address[0].zip + "\t")
                    f.write(contact.address[0].streetNumber + " " + contact.address[0].streetName + "\t")
                    f.write("\t")#f.write(contact.address[0].secondLine + "\t")# second line not implemented yet
                    f.write(contact.fname + " " + contact.lname + "\t")
                    f.write("\n")





