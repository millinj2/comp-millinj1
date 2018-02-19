from newspaper import Article
import datetime
import urllib.request
import sqlite3

def openFile(file):
# read a list, return a dic
    try: #is the file there??
        data = open(file, "r").read() #returns a string
        return data
    except IOError:
        print ("  \aNo such file!!!! \"",file,"\" so exiting")
        sys.exit(1)
#end of openFile()

def saveData(dt, art_hdl, article, filename):
#create the file
    f = open(filename,"w")
#write the data
    f.write(dt+"\n")
    f.write(art_hdl+"\n")
    f.write(article+"\n")
#close the file
    f.close()

def begin(inFile):
    source = open(inFile,"r").read() # load the whole file.
    source = openFile(inFile)

    print("is this working?")

    article.parse()
    article.html
    article.nlp()

    summary = article.summary
    filename = "articlesummary.txt"
    #create the file
    f = open(filename,"w")
    #write the data
    f.write(str(summary))
    dt = article.publish_date
    art_hdl = article.headline
    article = article.summary
    stock = "Apple"
    DBfileName = "../compDB.db"

    baggagehand(dt, company, art_hdl, article, DBfileName)

def baggagehand(dt, company, art_hdl, article, DBfileName):
# method to get a file, open content, and populate database

    print (" Baggagehand() We are saving to this file: ", DBfileName)
    # print " Data: "
    # print " StockID:" ,stockid
    # print " Value: ", stockValue
    # print " Date: ", dt


    sqlite_file = DBfileName # the database file.

    conn = sqlite3.connect(sqlite_file) # load the database file, defined above
    c = conn.cursor()

    c.execute("INSERT INTO news VALUES (?, ?, ?, ?)", (dt, company, art_hdl, article))
    conn.commit()
    #print the tables from database
    result = c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    print(result)
    #print everything in Stocks
    result2 = c.execute("SELECT * FROM news").fetchall()
    print (result2)
    row = c.fetchall()

    conn.close()


import sys

if __name__ == '__main__':
    url = 'http://fortune.com/2018/02/17/apple-homepod-iphone-sales/'
    article = Article(url)
    article.download()
    response = urllib.request.urlopen(url)

    data = response.read()
    text = repr(data).encode('utf-8')
    file_ = open('article.html', 'wb')
    file_.write(data)
    file_.close()

    # words = article.keywords
    # filename = "articlekeywords.txt"
    # #create the file
    # f = open(filename,"w")
    # #write the data
    # f.write(str(words))

    if len(sys.argv) == 2:
         begin(sys.argv[1]) #,sys.argv[3], sys.argv[4]),sys.argv[5])
    else:
         sys.exit(0)

    # summary = article.summary
    # filename = "articlesummary.txt"
    # #create the file
    # f = open(filename,"w")
    # #write the data
    # f.write(str(summary))
