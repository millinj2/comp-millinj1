#!/usr/bin/python

# questions: obonhamcarter@allegheny.edu
# date: 1 Feb 2018

#ref: https://www.google.com/search?biw=1134&bih=658&ei=tXlzWvPwBo24zwLLgYS4Cw&q=apple+stock&oq=apple&gs_l=psy-ab.1.0.0i131i67k1j0i67k1l3j0l5j0i131k1.20822.21239.0.23377.5.4.0.1.1.0.163.489.1j3.4.0....0...1c.1.64.psy-ab..1.4.338....0.DcZ6ZiTn6ms

import urllib2

def getStockValue(source):
# a home-made stock market value parser.

    start = source.find("g-unit")
    start = source.find("ref_284784_l", start + 1)
    start = source.find('>', start + 1)
    value = source[start:source.find('<',start + 1)]

    value = value.replace('"',"")
    value = value.replace("'","")

    print "stock Value :",value
    return value
# end of getStockValue()


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
    print "Loaded file,", inFile," Stockmarketprice:"
    source = open(inFile,"r").read() # load the whole file.
    source = openFile(inFile) # load the whole file.
    stockValue = getStockValue(source)

    print "  Loaded file,", inFile,"\n  Stock market price:",stockValue
# end of begin()



######### program command line init ########

import sys

if __name__ == '__main__':
#       if len(sys.argv) == 2: #one option added to command line
#       begin(sys.argv[1])

    response = urllib2.urlopen('https://finance.google.com/finance?q=intel&ei=4rV0WoCXIoW3e5_fuqgP')
    data = response.read()
    filename = "intel.html"
    file_ = open(filename, 'w')
    file_.write(data)
    file_.close()

    if len(sys.argv) == 2:
         begin(sys.argv[1])#,sys.argv[3], sys.argv[4]),sys.argv[5])
    else:
         giveHelp()
         sys.exit(0)
