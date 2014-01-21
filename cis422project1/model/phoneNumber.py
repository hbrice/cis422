__author__ = 'lucasr'

class phoneNumber:
    """docstring for phoneNumber"""
    def __init__(self, phoneType, number):
        self.phoneType = phoneType
        self.number = number

    def __eq__(self, other):
        return (self.phoneType == other.phoneType) and (self.number == other.number)
