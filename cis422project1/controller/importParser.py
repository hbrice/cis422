#input format The import/export format standard format will be a TAB separated list of entry fields. 
#tab seperated entry\n
#tab seperated entry\n
#...

#given an input line, determine if it is valid
def isValidInput(inputString):
    #DEFINITELY not good enough. It will work for now though.
    if inputString:
        return True
    else:
        return False

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
