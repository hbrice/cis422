__author__ = 'lucasr'
import os, sys

import os, sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

from address import address

def main():
    last = "Trentwood OR 94501"
    delivery = "1402 SW Alder st."
    second = "APT 11"
    test = address(last, delivery, second)
    print(test)
    print(test.addressNumber)
    print(test.address)
    print(test.city)
    print(test.state)
    print(test.zip)
    last2 = "Oakland CA 94501"
    delivery2 = "1235 Broadway st."
    second2 = " "
    test2 = address(last2, delivery2, second2)
    test3 = address(last2, delivery2, second2)
    print(test2)
    print(test2.addressNumber)
    print(test2.address)
    print(test2.city)
    print(test2.state)
    print(test2.zip)
    print(test==test2)
    print(test2==test3)
    print("OR" in test)
    print("or" in test2)
if __name__ == '__main__':
    main()
