#!/usr/bin/python

import urllib2
import datetime
import sqlite3

def getStockValue(source):
# a home-made stock market value parser.

    start = source.find("g-unit")
    start = source.find("ref_284784_l", start + 1)
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
def saveData(stockid, stockValue, dt, filename):
#create the file
    f = open(filename,"w")
#write the data
    f.write(stockid+"\n")
    f.write(stockValue+"\n")
    f.write(dt+"\n")
    # f.write(time+"\n")
#close the file
    f.close()

def begin(inFile):
#infile is the name of the html file that is saved from google's stock page
    source = open(inFile,"r").read() # load the whole file.
    source = openFile(inFile) # load the whole file.
    stockValue = getStockValue(source)
    stockid = getStockID(source)
    now = datetime.datetime.now()
    dt = now.strftime("%Y-%m-%d--%H:%M")
    #time = now.strftime("%I:%M %p")
    stock = "Intel"
    filename = "intelfiles/IntelData-" + dt +".txt"
    DBfileName = "../compDB.db"

    # print " Stock ID:",stockid ,"\n Stock market price:",stockValue
    # print " Date",dt
    # print " Time",time

    saveData(stockid, stockValue, dt, filename)
    baggagehand(stockid, stockValue, dt, DBfileName)

# end of begin()

######### program command line init ########

def baggagehand(stockid, stockValue, dt, DBfileName):
# method to get a file, open content, and populate database

    print " Baggagehand() We are saving to this file: ",DBfileName
    # print " Data: "
    # print " StockID:" ,stockid
    # print " Value: ", stockValue
    # print " Date: ", dt
    # print " Time: ", time

    sqlite_file = DBfileName # the database file.

    conn = sqlite3.connect(sqlite_file) # load the database file, defined above
    c = conn.cursor()

    c.execute("INSERT INTO stocks VALUES ('dt', 'stock', 'stockid', 'stockValue')")
    row = c.fetchall()

   #  for line_list in row:
	# print "\nline_list = ",line_list,type(line_list)
   #  line_list =  (u'10114', u'Maximillian', u'S5', u'Biology', 86000) <type 'tuple'>
	# count = 0
	# for i in line_list:
	# 	count = count + 1
	# 	print "  Tuple Position in line_list :", count,"::",i
   # conn.close()


# end of baggagehand()

######### program command line init ########

import sys

if __name__ == '__main__':
#       if len(sys.argv) == 2: #one option added to command line
#       begin(sys.argv[1])

    response = urllib2.urlopen('https://finance.google.com/finance?q=intel&ei=4rV0WoCXIoW3e5_fuqgP')
    data = response.read()
    filename = "intelfiles/intel.html"
    file_ = open(filename, 'w')
    file_.write(data)
    file_.close()

    if len(sys.argv) == 2:
         begin(sys.argv[1])#,sys.argv[3], sys.argv[4]),sys.argv[5])
    else:
         giveHelp()
         sys.exit(0)
