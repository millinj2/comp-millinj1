from newspaper import Article
import datetime
import urllib.request
import sqlite3
import csv
import sys
from textblob import TextBlob

def getArticleSummary(source):
    article.parse()
    article.html
    article.nlp()

    value1 = article.summary
    return value1

def getArticleDate(source):
    article.parse()
    article.html
    article.nlp()
    value2 = article.publish_date
    return value2

def getKeyWords(source):
    article.parse()
    article.html
    article.nlp()
    words = article.keywords
    filename = "articlekeywords.txt"
    #create the file
    f = open(filename,"w")
    #write the data
    f.write(str(words))

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

    article = getArticleSummary(source)
    filename = "articlesummary.csv"
    #create the file
    f = open(filename,"w")
    #write the data
    f.write(str(article))
    dt = getArticleDate(source)
    art_hdl = "Article Headline2"#getArticleHeadline(source)
    company = "Apple"
    DBfileName = "../compDB.db"

    baggagehand(dt, company, art_hdl, article, DBfileName)

# def baggagehand(dt, company, art_hdl, article, DBfileName):
# # method to get a file, open content, and populate database
#
#     print (" Baggagehand() We are saving to this file: ", DBfileName)
#     # print " Data: "
#     # print " StockID:" ,stockid
#     # print " Value: ", stockValue
#     # print " Date: ", dt
#
#     sqlite_file = DBfileName # the database file.
#
#     conn = sqlite3.connect(sqlite_file) # load the database file, defined above
#     c = conn.cursor()
#
#     c.execute("INSERT INTO news VALUES (?, ?, ?, ?)", (dt, company, art_hdl, article))
#     conn.commit()
#     #print the tables from database
#     result = c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
#     print(result)
#     #print everything in Stocks
#     result2 = c.execute("SELECT * FROM news").fetchall()
#     print (result2)
#     row = c.fetchall()
#
#     conn.close()

# def baggagehandModel(stock_ID, art_hdl, sentiscore, keywords, DBfileName):
# # method to get a file, open content, and populate database
#
#     print (" Baggagehand() We are saving to this file: ", DBfileName)
#     # print " Data: "
#     # print " StockID:" ,stockid
#     # print " Value: ", stockValue
#     # print " Date: ", dt
#
#     sqlite_file = DBfileName # the database file.
#
#     conn = sqlite3.connect(sqlite_file) # load the database file, defined above
#     c = conn.cursor()
#
#     c.execute("INSERT INTO news VALUES (?, ?, ?, ?)", (dt, company, art_hdl, article))
#     conn.commit()
#     #print the tables from database
#     result = c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
#     print(result)
#     #print everything in Stocks
#     result2 = c.execute("SELECT * FROM news").fetchall()
#     print (result2)
#     row = c.fetchall()
#
#     conn.close()

def sentAnalysis:
    # to force utf-8 encoding on entire program
    reload(sys)
    sys.setdefaultencoding('utf8')

    with open('/Users/jennamillin/repos/cs600/comp-millinj2/articlesummary.csv', 'r') as fp:
         content = fp.read()
    blob = TextBlob(content)
    print blob.sentiment.polarity

#make files to save the polarity and subjectivity


#https://planspace.org/20150607-textblob_sentiment/

import sys

if __name__ == '__main__':
    url = 'http://fortune.com/2018/02/17/apple-homepod-iphone-sales/'
    article = Article(url)
    article.download()
    response = urllib.request.urlopen(url)

    data = response.read()
    text = repr(data).encode('utf-8')
    filename = "article.html"
    file_ = open(filename, 'wb')
    file_.write(data)
    file_.close()

    if len(sys.argv) == 1:
         begin(sys.argv[0]) #,sys.argv[3], sys.argv[4]),sys.argv[5])
    else:
         sys.exit(0)
