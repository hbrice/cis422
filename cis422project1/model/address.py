__author__ = 'lucasr'

class address:
    """docstring for address"""
    def __init__(self, last, delivery, second):
        # Last: City State Zip
        # Delivery: 1401 SW Main St.
        # Second: " " or APT 4
        self.last = last.lower()
        self.delivery = delivery.lower()
        self.second =  second.lower()
        self.zip = self.last.lower().split(" ")[2]

    def __eq__(self, other):
        return (self.last and other.last) and (self.delivery == other.delivery) \
            and (self.second.lower() == other.second.lower())

    def __contains__(self, item):
        return (item in self.last) or (item in self.delivery) \
            or (item in self.second) or (item in self.zip)