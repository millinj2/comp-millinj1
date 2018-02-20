#!/bin/bash


  cd /Users/jennamillin/repos/cs600/comp-millinj2/stockret
  python scrapAmazon.py amazon.html
  cd /Users/jennamillin/repos/cs600/comp-millinj2/stockret
  python scrapApple.py apple.html
  cd /Users/jennamillin/repos/cs600/comp-millinj2/stockret
  python scrapGoogle.py google.html
  cd /Users/jennamillin/repos/cs600/comp-millinj2/stockret
  python scrapIBM.py ibm.html
  cd /Users/jennamillin/repos/cs600/comp-millinj2/stockret
  python scrapIntel.py intel.html
  cd /Users/jennamillin/repos/cs600/comp-millinj2/stockret
  python scrapMicrosoft.py microsoft.html

#  python database.py


# chmod +x getData.txt
