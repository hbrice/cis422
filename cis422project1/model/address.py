__author__ = 'lucasr'

class address:
    """docstring for address"""
    def __init__(self, last, delivery, second):
        # Last: City State Zip
        # Delivery: 1401 SW Main St.
        # Second: " " or APT 4
        self.last = last
        self.delivery = delivery
        self.second =  second

    def __eq__(self, other):
        return (self.last and other.last) and (self.delivery == other.delivery) \
            and (self.second.lower() == other.second.lower())

    '''def __contains__(self, item):
        return (item == self.addressType) or (item == self.streetNumber) or \
        (item == self.streetName) or (item == self.city) or \
        (item == self.state) or (item == self.zip)'''

