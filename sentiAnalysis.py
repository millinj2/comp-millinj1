import csv
import sys
from textblob import TextBlob

# to force utf-8 encoding on entire program
reload(sys)
sys.setdefaultencoding('utf8')

with open('/Users/jennamillin/repos/cs600/comp-millinj2/articlesummary.csv', 'r') as fp:
     content = fp.read()
blob = TextBlob(content)
print blob.sentiment.polarity

#make files to save the polarity and subjectivity


#https://planspace.org/20150607-textblob_sentiment/
