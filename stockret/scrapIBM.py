#!/usr/bin/python

import urllib2
import datetime
import sqlite3

def getStockValue(source):
# a home-made stock market value parser.

    start = source.find("g-unit")
    start = source.find("ref_18241_l", start + 1)
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
    print "\t\tA program to parse Stocks pages for the stock market price."
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
    stockid = stockid.replace(",","")
    stockValue = stockValue.replace(",","")
    dt = dt.replace(",","")
    f.write(stockid+ ",")
    f.write(stockValue+",")
    f.write(dt)
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
    dt = now.strftime("%Y-%m-%d--%H:%M-IBM")
    #time = now.strftime("%I:%M %p")
    stock = "IBM"
    filename = "ibmfiles/IBMData-" + dt +".txt"
    DBfileName = "../compDB.db"

    # print " Stock ID:",stockid ,"\n Stock market price:",stockValue
    # print " Date",dt
    # print " Time",time

    saveData(stockid, stockValue, dt, filename)
    baggagehand(stock, stockid, stockValue, dt, DBfileName)

# end of begin()

######### program command line init ########

def baggagehand(stock, stockid, stockValue, dt, DBfileName):
# method to get a file, open content, and populate database

    print " Baggagehand() We are saving to this file: ",DBfileName
    print " Data: "
    print " StockID:" ,stockid
    print " Value: ", stockValue
    print " Date: ", dt


    sqlite_file = DBfileName # the database file.

    conn = sqlite3.connect(sqlite_file) # load the database file, defined above
    c = conn.cursor()

    c.execute("INSERT INTO stocks VALUES (?, ?, ?, ?)", (dt, stock, stockid, stockValue))
    conn.commit()
    #print the tables from database
    result = c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    print result
    #print everything in Stocks
    # result2 = c.execute("SELECT * FROM stocks").fetchall()
    # print result2
    row = c.fetchall()

    conn.close()
# end of baggagehand()

######### program command line init ########

import sys

if __name__ == '__main__':
#       if len(sys.argv) == 2: #one option added to command line
#       begin(sys.argv[1])

    response = urllib2.urlopen('https://finance.google.com/finance?q=NYSE%3AIBM&ei=EbR0WrCiGcrae_OCppgP')
    data = response.read()
    filename = "ibm.html"
    file_ = open(filename, 'w')
    file_.write(data)
    file_.close()

    if len(sys.argv) == 2:
         begin(sys.argv[1])#,sys.argv[3], sys.argv[4]),sys.argv[5])
    else:
         giveHelp()
         sys.exit(0)
