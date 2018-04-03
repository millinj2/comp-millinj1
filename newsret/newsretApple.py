#!/usr/bin/env python3
from newspaper import Article
import datetime
import urllib.request
from urllib.request import Request, urlopen
import sqlite3
import csv
import sys
# from textblob import TextBlob

def getArticleSummary(source):
    print(source)
    article.parse()
    article.html
    article.nlp()

    value1 = article.summary
    print("this is the summary")
    print(value1 + "\n")

    # art_summary = value1
    # auth = str(article.authors)
    # filename = "articleSummaryFiles/article" + auth + "summary.csv"
    # #create the file
    # f = open(filename,"w")
    # #write the data
    # f.write(str(article))
    # dt = getArticleDate(source)
    # DBfileName = "../compDB.db"
    # ref = str(url)
    #
    # print("about to write to database")
    # baggagehand(dt, company, ref, art_summary, DBfileName

    return value1


def getArticleDate(source):
    article.parse()
    article.html
    article.nlp()

    value2 = article.publish_date
    print(value2)
    print("\n")

    return value2


def getKeyWords(source):
    article.parse()
    article.html
    article.nlp()
    words = article.keywords
    auth = str(article.authors)
    filename = "keywords/Apple/article" + company + auth + "keywords.txt"
    #create the file
    f = open(filename,"w")
    #write the data
    f.write(str(words))

    dt = str(getArticleDate(source))
    art_summary = getArticleSummary(source)

    # art_summary = value1
    auth = str(article.authors)
    print(auth)
    ref = str(url)
    print(ref)
    counter = 0

    if auth == False:
        # for filename in filname:
        filename = "articleSummaryFiles/Apple/article" + company + str(counter) + "summary.csv"
        counter += 1
    else:
        filename = "articleSummaryFiles/Apple/article" + company + auth + str(counter) + "summary.csv"
        counter += 1
    #create the file
    f = open(filename,"w")
    #write the data
    f.write(str(art_summary))
    art_sum_name = filename

    saveData(dt, url, art_summary, company, art_sum_name, filename)
    # baggagehand(dt, company, ref, art_summary, DBfileName)

    print(words)
    return words

def openFile(file):
# read a list, return a dic
    try: #is the file there??
        data = open(file, "r").read() #returns a string
        return data
    except IOError:
        print ("  \aNo such file!!!! \"",file,"\" so exiting")
        sys.exit(1)
#end of openFile()
    saveData(dt, url, art_summary, company, art_sum_name, filename)

def saveData(dt, url, art_summary, company, art_sum_name, filename):
#create the file
    f = open(filename,"w")
    nl = "\n"
#write the data
    if dt is not None:
        f.write(dt)
        f.write("\n")
        f.write(art_summary + nl)
        # f.write("\n")
        f.write(url + nl)
        # f.write("\n")
        f.write(company + nl)
        # f.write("\n")
        f.write(art_sum_name)
    else:
        f.write(art_summary + nl)
        # f.write("\n")
        f.write(url + nl)
        # f.write("\n")
        f.write(company + nl)
        # f.write("\n")
#close the file
    f.close()
    print("file saved")

    dt = str(getArticleDate(article))
    DBfileName = "../compDB.db"
    ref = str(url)

    print("about to write to database")

    baggagehand(dt, company, ref, art_summary, art_sum_name, DBfileName)


def begin(inFile):
    source = open(inFile,"r").read() # load the whole file.
    source = openFile(inFile)

    art_summary = getArticleSummary(source)
    auth = str(article.authors)
    filename = "articleSummaryFiles/Apple/article" + auth + "summary.csv"
    #create the file
    f = open(filename,"w")
    #write the data
    f.write(str(article))
    dt = getArticleDate(source)
    ref = str(url)
    DBfileName = "../compDB.db"

    print("about to write to database")

    # baggagehand(dt, company, ref, art_summary, art_sum_name, DBfileName)

def baggagehand(dt, company, ref, art_summary, art_sum_name, DBfileName):
# method to get a file, open content, and populate database

    print (" Baggagehand() We are saving to this file: ", DBfileName)

    sqlite_file = DBfileName # the database file.

    conn = sqlite3.connect(sqlite_file) # load the database file, defined above
    c = conn.cursor()

    c.execute("INSERT OR IGNORE INTO news VALUES (?, ?, ?, ?, ?)", (dt, company, ref, art_summary, art_sum_name))
    conn.commit()
    #print the tables from database
    result = c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    # print(result)
    #print everything in Stocks
    # result2 = c.execute("SELECT * FROM news").fetchall()
    # print (result2)
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

    inFile1 = "appleDataUrls.txt" # use a parameter from the terminal?
    data_list = openFile2(inFile1) # get a list of the links from the data.txt

    for i in data_list:
        try:
            x = urllib.request.urlopen(i)
            url = i
            # print(" Send this url = ",url," to your newspaper code using a for loop like this...")
            # url = 'https://www.mediapost.com/publications/article/315144/amazon-seeks-startups-for-alexa-innovations.html'
            article = Article(url)
            article.download()
            response = urllib.request.urlopen(url)
            company = "Apple"
            print(url)

            getArticleSummary(article)
            print("does this work")
            getArticleDate(url)
            print("how about this")
            getKeyWords(article)
            # print("or this?")
            # openFile(file)
            # saveData(dt, url, art_summary, company, filename)
            # begin(inFile)

        except urllib.error.HTTPError as e:
            if e.code in (..., 403, ...):
                continue

        # article = Article(url)
        # article.download()
        # response = urllib.request.urlopen(url)
        #
        # getArticleSummary(url)
        # getArticleDate(url)
        # getKeyWords(url)
        # openFile(file)
        # saveData(dt, url, art_summary, company, filename)
        # begin(inFile)

    # article = Article(url)
    # article.download()
    # response = urllib.request.urlopen(url)
    # company = "Apple"
    #
    # getArticleSummary(url)
    # getArticleDate(url)
    # getKeyWords(url)


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
