__author__ = 'lucasr'
from model import contact

class addressbook:
    """docstring for addressbook"""
    def __init__(self):
        self.contacts = []

    def addContact(self, contact):
        self.contacts.append(contact)

    def findContactByName(self, fname, lname):
        tmp = contact(fname, lname)
        indices = [i for i, val in enumerate(self.contacts) if val == tmp]
        if (len(indices) > 1):
             print("More than one contact found:")
             for i in indices:
                print(i, " ", self.contacts[indices[i]])
        else:
            print(self.contacts[indices])

    #def generalSearchContacts(self, keyword):
        #for i in self.contacts:

    def removeContact(self, contact):
        self.contacts.remove(contact)

    def removeContactByName(self, fname, lname):
        tmp = contact(fname, lname)
        indices = [i for i, val in enumerate(self.contacts) if val == tmp]
        if (len(indices) > 1):
            print("More than one contact found:")
            for i in indices:
                print(i, " ", self.contacts[indices[i]])
            idx = input("Please specify by index for the correct contact to delete. "
                        "Or type 'all' to delete all contacts found: ")
            if idx != "all":
                try:
                    del self.contacts[idx]
                except ValueError:
                    print("Not a correct index!")
            else:
                for i in indices:
                    del self.contacts[indices[i]]
        else:
            del self.contacts[indices]

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





