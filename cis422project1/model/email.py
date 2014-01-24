__author__ = 'lucasr'

class email:
    """docstring for email"""
    def __init__(self, emailType, addr):
        self.emailType = emailType
        self.addr =  addr

    def __eq__(self, other):
        return (self.emailType == other.emailType) and (self.addr.lower() == other.addr.lower())