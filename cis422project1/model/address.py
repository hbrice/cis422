__author__ = 'lucasr'

class address:
    """docstring for address"""
    def __init__(self, addressType, streetNumber, streetName, city, state, zip):
        self.addressType = addressType
        self.streetNumber = streetNumber
        self.streetName = streetName
        self.city = city
        self.state = state
        self.zip = zip

    def __eq__(self, other):
        return (self.addressType and other.addressType) and (self.streetNumber == other.streetNumber) \
            and (self.streetName == other.streetName) and (self.city == other.city) \
            and (self.state == other.state) and (self.zip == other.zip)
