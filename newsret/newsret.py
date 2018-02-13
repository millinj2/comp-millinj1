from lxml import html
import requests
import urllib2


def getNewsart(source):
    start = source.find("html")
    start = source.find("head")
    start = source.find("title", start+1)
    start = source.find(">", start + 1)
    value = source[start:source.find('>',start +1)]

    value = value.replace('"',"")
    value = value.replace("'","")

    value = value.replace(">","")
    value = value.replace("<","")


    return value

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
    source = open(inFile,"r").read() # load the whole file.
    source = openFile(inFile) # load the whole file.
    headline = getNewsart(source)

    print headline

import sys

if __name__ == '__main__':

    response = urllib2.urlopen('https://gizmodo.com/waymo-uber-settle-lawsuit-over-automated-vehicle-trade-1822869082')
    data = response.read()
    filename = "test.html"
    file_ = open(filename, 'w')
    file_.write(data)
    file_.close()

    if len(sys.argv) == 2:
         begin(sys.argv[1])#,sys.argv[3], sys.argv[4]),sys.argv[5])
    else:
         sys.exit(0)




# # Parse the html from the webpage
# pagehtml = html.fromstring(response.text)
#
# # search for news headlines
# news = pagehtml.xpath('//h2[@class="esc-lead-article-title"] \
#                   /a/span[@class="titletext"]/text()')
#
# # Print each news item in a new line
# print("\n \n".join(news))
#
# tf = open("headlines.txt", "w")
#
# tf.write("\n \n".join(news).lower())
#
# tf.close()
# # puts as lower case in text file named headlines
#
# with open('headlines.txt', 'r') as inF:
#     for line in inF:
#         if 'inflation' in line:
#              print "\n" + "    " + line
