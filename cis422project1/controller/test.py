import importParser
import sys

def main():
    print sys.argv
    f = open(sys.argv[1], 'rb')
    d = importParser.importParse(f)
    print d

if __name__ == "__main__":
    main()
