#import scrapAmazon
# import scrapApple
# import scrapGoogle from scrapGoogle
# import scrapIBM from scrapIBM
# import scrapIntel from scrapIntel
# import scrapMicrosoft from scrapMicrosoft

import sqlite3
conn = sqlite3.connect('compDB.db')

c = conn.cursor()
#
c.execute('''CREATE TABLE stocks(
          dt  VARCHAR NOT NULL,
          stock VARCHAR(20) NOT NULL,
          stock_ID VARCHAR(10) NOT NULL,
          stockValue VARCHAR(10) NOT NULL,
          PRIMARY KEY(dt),
          FOREIGN KEY(stock_ID) REFERENCES model(stock_ID))''')

c.execute('''CREATE TABLE news(
          company VARCHAR(20) NOT NULL,
          art_hdl VARCHAR(100) NOT NULL,
          article VARCHAR NOT NULL,
          PRIMARY KEY(art_hdl),
          FOREIGN KEY(art_hdl) REFERENCES model(art_hdl))''')

c.execute('''CREATE TABLE model(
          stock_ID VARCHAR(10) NOT NULL,
          art_hdl VARCHAR(100) NOT NULL,
          sentiscore INTEGER(10) NOT NULL,
          key_words VARCHAR NOT NULL,
          PRIMARY KEY(stock_ID),
          FOREIGN KEY(stock_ID) REFERENCES stocks(stock_ID),
          FOREIGN KEY(art_hdl) REFERENCES news(art_hdl))''')

# for p in stockinfo:
#     format_str = """INSERT INTO stocks (dt, stock, stock_ID, stk_chg)
#     VALUES ("{time}", "{stock}", "{stockid", "{stockValue}");"""
#
#     sql_command = format_str.format(time=p[0], stock=p[1], stockid=p[2], stockValue = p[3])
#     cursor.execute(sql_command)

# c.execute("INSERT INTO stocks VALUES ("{dt}", "{stock}", "{stockid}", "{stockValue}")")
