import csv
import sys
import os
import codecs
from textblob import TextBlob

# to force utf-8 encoding on entire program
reload(sys)
sys.setdefaultencoding('utf8')

with open('/Users/jennamillin/repos/cs600/comp-millinj2/articleAmazon[\'Chuck Matrti\']0summary.csv', 'r') as fp:
    content = fp.read()
    blob = TextBlob(content)
    print blob.sentiment
    print blob.sentiment.polarity
