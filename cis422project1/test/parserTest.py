import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../controller'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

import utils

def main():
    print sys.argv
    f = open(sys.argv[1], 'rb')
    d = utils.importParse(f)
    print d

if __name__ == "__main__":
    main()
