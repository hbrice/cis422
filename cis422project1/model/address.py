__author__ = 'lucasr'

class address:
    """docstring for address"""
    def __init__(self, last, delivery, second):
        # Last: City State Zip
        # Delivery: 1401 SW Main St.
        # Second: " " or APT 4
        self.last = last.lower()
        self.delivery = delivery.lower()
        self.second = second.lower()
        parsedLast = self.parseLast(self.last)
        self.addressNumber = self.delivery.split(" ")[0]
        self.address = ' '.join(self.delivery.split(" ")[1:])
        self.city = parsedLast[0]
        self.state = parsedLast[1]
        self.zip = parsedLast[2]

    def __eq__(self, other):
        return (self.last == other.last) and (self.delivery == other.delivery) \
            and (self.second.lower() == other.second.lower())

    def __str__(self):
        if (self.second != " "):
            return self.delivery + " " + self.second + " " + self.last
        else:
            return self.delivery + " " + self.last

    def __repr__(self):
        if (self.second != " "):
            return self.delivery + " " + self.second + " " + self.last
        else:
            return self.delivery + " " + self.last

    def __contains__(self, item):
        return (item.lower() in self.last) or (item.lower() in self.delivery) \
            or (item.lower() in self.second)

    def parseLast(self, last):
        # EXAMPLE:
        # SAN DIEGO CA 97201
        #  0    1    2    3
        output = []
        tmp = last.split(" ")
        idx = 0
        for i in tmp:
            if(i.isdigit()):
                output.append(tmp[idx])
                output.append(tmp[idx-1])
                output.append(' '.join(tmp[0:idx-1]))
            else: idx += 1
        return output