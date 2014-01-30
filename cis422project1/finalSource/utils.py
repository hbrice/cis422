#input format The import/export format standard format will be a TAB separated list of entry fields. 
#tab seperated entry\n
#tab seperated entry\n
#...
import tkMessageBox
#The expected header. We can toss anything else out
_HEADER="Last\tDelivery\tSecond\tRecipient\tPhone"

#given an .tsv file will output a list of maps
def importParse(importFile):
    entryList = list()
    firstLine = True
    header = importFile.readline()

    if _HEADER in header:
        inputFormat = _HEADER.rstrip().split('\t')
        lines = importFile.readlines()
        for line in lines:
            #This line is a doozy: first grab the line, strip any trailing whitespace, split it on tabs. 
            #Then make a list of tuples from the input format and that resulting list, turn that into a map, finally append that map to the entrylist
            entryList.append(dict(zip(inputFormat, line.rstrip().split('\t'))))
        return entryList
    else:
        tkMessageBox.showinfo("Alert", "Invalid Header in import file", icon='warning')
