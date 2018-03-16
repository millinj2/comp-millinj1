from newspaper import Article
import datetime
import urllib.request
import sqlite3
import csv
import sys
# from textblob import TextBlob

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

def saveData(dt, url, art_summary, company, filename):
#create the file
    f = open(filename,"w")
#write the data
    f.write(dt+"\n")
    f.write(art_summary+"\n")
    f.write(url++"\n")
    f.write(company+"\n")
#close the file
    f.close()

def begin(inFile):
    source = open(inFile,"r").read() # load the whole file.
    source = openFile(inFile)

    art_summary = getArticleSummary(source)
    auth = str(article.authors)
    filename = "articleSummaryFiles/article" + auth + "summary.csv"
    #create the file
    f = open(filename,"w")
    #write the data
    f.write(str(article))
    dt = getArticleDate(source)
    DBfileName = "../compDB.db"

    baggagehand(dt, company, url, art_summary, DBfileName)

def baggagehand(dt, company, url, art_summary, DBfileName):
# method to get a file, open content, and populate database

    print (" Baggagehand() We are saving to this file: ", DBfileName)

    sqlite_file = DBfileName # the database file.

    conn = sqlite3.connect(sqlite_file) # load the database file, defined above
    c = conn.cursor()

    c.execute("INSERT INTO news VALUES (?, ?, ?, ?)", (dt, company, url, art_summary))
    conn.commit()
    #print the tables from database
    result = c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    print(result)
    #print everything in Stocks
    result2 = c.execute("SELECT * FROM news").fetchall()
    print (result2)
    row = c.fetchall()

    conn.close()


# def sentAnalysis:
#     # to force utf-8 encoding on entire program
#     reload(sys)
#     sys.setdefaultencoding('utf8')
#
#     with open('/Users/jennamillin/repos/cs600/comp-millinj2/articlesummary.csv', 'r') as fp:
#          content = fp.read()
#     blob = TextBlob(content)
    # print blob.sentiment.polarity

#make files to save the polarity and subjectivity


#https://planspace.org/20150607-textblob_sentiment/

def openFile2(inFile1):
    #fname = "data.txt"
    #f_list = open(fname,"r").readlines() #each line from the file is a link
    f_list = open(inFile1,"r").readlines() #each line from the file is a link

    #clean each element of list, remove line feeds ("\n")

    data_list = [] #define a list
    for i in f_list:
        tmp = i.replace("\n","")
        data_list.append(tmp)

    # print "clean data :",data_list

    return data_list
# end of openFile2()

import sys

if __name__ == '__main__':

    # inFile1 = "amazonDataUrls.txt" # use a parameter from the terminal?
    # data_list = openFile2(inFile1) # get a list of the links from the data.txt
    #
    # for i in data_list:
    #     print(i)
    #     url = i
    #     print(" Send this url = ",url," to your newspaper code using a for loop like this...")

    url = 'https://www.mediapost.com/publications/article/315144/amazon-seeks-startups-for-alexa-innovations.html'
    article = Article(url)
    article.download()
    response = urllib.request.urlopen(url)

    company = "Amazon"

    # data = response.read()
    # text = repr(data).encode('utf-8')
    # filename = "article.html"
    # file_ = open(filename, 'wb')
    # file_.write(data)
    # file_.close()

    if len(sys.argv) == 1:
         begin(sys.argv[0]) #,sys.argv[3], sys.argv[4]),sys.argv[5])
    else:
         sys.exit(0)
