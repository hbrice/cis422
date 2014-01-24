#input format The import/export format standard format will be a TAB separated list of entry fields. 
#tab seperated entry\n
#tab seperated entry\n
#...

#given an input line, determine if it is valid
def isValidInput(inputString, inputFormat):
    #A line is valid if not all fields are blank and the address is in the USPS standard format
    #...Testing to see if an address is valid is really hard
    if inputString:
        return True
    else:
        return False

#given an .tsv file will output a list of maps
def importParse(importFile):
    entryList = list()
    firstLine = true
    header = importFile.readline()
    inputFormat = header.rstrip().split('\t')
    lines = importFile.readlines()[1:]
    for line in lines:
        if isValidInput(line):
            #This line is a doozy: first grab the line, strip any trailing whitespace, split it on tabs. 
            #Then make a list of tuples from the input format and that resulting list, turn that into a map, finally append that map to the entrylist
            entryList.append(dict(zip(inputFormat, line.rstrip().split('\t'))))
        else:
            print line + " is invalid."
    return entryList

"""
#given a file will output a list of maps
def importParse(importFile):
    _FORMAT = ["fname","lname","addr","city","state","zip","phone","email"]
    entryList = list()
    for line in importFile:
        #split the line on tab characters
        #turn it into a map with the format list as the keys
        #add it to the list
        if isValidInput(line):
            print line.split('\t'), "\n"
            print zip(_FORMAT, line.split('\t')), "\n"
            entryList.append(dict(zip(_FORMAT, line.split('\t'))))
        else:
            print "'", line, "' is invalid."
    if not entryList:
        print "Empty input"
    return entryList
"""
