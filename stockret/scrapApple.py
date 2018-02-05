#!/usr/bin/python

import urllib2
import datetime

def getStockValue(source):
# a home-made stock market value parser.

    start = source.find("g-unit")
    start = source.find("ref_22144_l", start + 1)
    start = source.find('>', start + 1)
    value = source[start:source.find('<',start + 1)]

    value = value.replace('"',"")
    value = value.replace("'","")

    value = value.replace(">","")
    value = value.replace("<","")

    return value
# end of getStockValue()

def getStockID(source):

    start = source.find("g-unit norm")
    start = source.find("searchmore", start + 1)
    start = source.find('>', start + 1)
    value2 = source[start:source.find('<',start + 1)]

    value2 = value2.replace('"',"")
    value2 = value2.replace("'","")

    value2 = value2.replace(">","")
    value2 = value2.replace("<","")

    return value2

def giveHelp():
    print "\t\tA program to parse Google Stocks pages for the stock market price."
    print "\t\tUsage: programName file.html"
    print "\tNote: the file.html is only the main website file of the stocks page, not the css files."
    print " "
#end of help()

def openFile(file):
# read a list, return a dic
        try: #is the file there??
                data = open(file, "r").read() #returns a string
                return data
        except IOError:
                print "  \aNo such file!!!! \"",file,"\" so exiting"
                sys.exit(1)
#end of openFile()


def begin(inFile):
#infile is the name of the html file that is saved from google's stock page
#starter file
    source = open(inFile,"r").read() # load the whole file.
    source = openFile(inFile) # load the whole file.
    stockValue = getStockValue(source)
    stockid = getStockID(source)
    now = datetime.datetime.now()

    print " Stock ID:",stockid ,"\n Stock market price:",stockValue
    print " Date ",now.strftime("%b,%m,%Y")


######### program command line init ########

import sys

if __name__ == '__main__':
#       if len(sys.argv) == 2: #one option added to command line
#       begin(sys.argv[1])

    response = urllib2.urlopen('https://finance.google.com/finance?q=NASDAQ%3AAAPL&ei=TJF0WqioCsODmAG5rLnYBg')
    data = response.read()
    filename = "apple.html"
    file_ = open(filename, 'w')
    file_.write(data)
    file_.close()

    if len(sys.argv) == 2:
         begin(sys.argv[1])#,sys.argv[3], sys.argv[4]),sys.argv[5])
    else:
         giveHelp()
         sys.exit(0)
