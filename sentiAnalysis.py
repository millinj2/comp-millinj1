import csv
import sys
import os
import codecs
from textblob import TextBlob

# to force utf-8 encoding on entire program
reload(sys)
# sys.setdefaultencoding('utf8')

path = "/Users/jennamillin/repos/cs600/comp-millinj2/newsret/articleSummaryFiles/Microsoft"

for filename in os.listdir(path):
    filename = os.path.join(path, filename)
    print filename
    with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as fp:
        # if fp.endswith(".csv"):
        content = fp.read()
        blob = TextBlob(content)
        print fp
        print blob.sentiment.polarity
        print "\n"

#make files to save the polarity and subjectivity


#https://planspace.org/20150607-textblob_sentiment/
