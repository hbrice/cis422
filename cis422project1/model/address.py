__author__ = 'lucasr'

import tkMessageBox

class address:

    def __init__(self, last, delivery, second):
        """
        Takes in last, delivery and second of a US Postal Standard Address
        Last: City State Zip
        Delivery: 1401 SW Main St.
        Second: " " or APT 4
        Makes every input lowercase for convention. The Last is parsed by calling the function parsedLast(last) function.
        See function for details. Delivery finds number the address number and then everything after is the street name.
        """
        self.last = last.lower()
        self.delivery = delivery.lower()
        self.second = second.lower()
        parsedLast = self.parseLast(self.last)
        self.addressNumber = self.delivery.split(" ")[0]
        self.address = ' '.join(self.delivery.split(" ")[1:])
        print(parsedLast[0])
        print(parsedLast[1])
        print(parsedLast[2])
        self.city = parsedLast[0]
        self.state = parsedLast[1]
        self.zip = parsedLast[2]

    def __eq__(self, other):
        """
        Equality function compares last, delivery and second with other address. All lowercase if everything is equal
        then both addresses are equal and will return True
        """
        return (self.last == other.last) and (self.delivery == other.delivery) \
            and (self.second.lower() == other.second.lower())

    def __str__(self):
        """
        Print function used for testing prints delivery<space>second<space>last or
        prints delivery<space>last if no second is given
        """
        if (self.second != " "):
            return self.delivery + " " + self.second + " " + self.last
        else:
            return self.delivery + " " + self.last

    def __repr__(self):
        """
        Same implementation as __str__ used for various cases when __str__ wouldn't print. Example: List of addresses
        """
        if (self.second != " "):
            return self.delivery + " " + self.second + " " + self.last
        else:
            return self.delivery + " " + self.last

    def __contains__(self, item):
        """
        Finds if a string is in either last, delivery or lower. Considers substrings of strings.
        Example: can find if "sw" is in delivery="sw main st."
        """
        return (item.lower() in self.last) or (item.lower() in self.delivery) \
            or (item.lower() in self.second)

    def parseLast(self, last):
        """
        Makes sure that last is parsed correctly, test cases when city has two words.
        EXAMPLE:
        SAN DIEGO CA 97201
        0    1    2    3
        will return a list with ["san diego", "ca", "97201"]
        """
        output = []
        tmp = last.split(" ")
        idx = (len(tmp)-1)
        if (tmp[len(tmp)-1].isdigit()):
            output.insert(0,tmp[idx])
            output.insert(0,tmp[idx-1])
            output.insert(0,' '.join(tmp[0:idx-1]))
        else:
            tkMessageBox.showinfo("Alert", "No Zip found in input!", icon='warning')
            output.insert(0,"0")
            output.insert(0,tmp[idx])
            output.insert(0,' '.join(tmp[0:idx]))
        return output