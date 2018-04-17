library(tidyverse)
library(dplyr)
library(readr)
library(qdap)


modelTable <- read_delim("modelTable.csv", "\t", escape_double = FALSE, trim_ws = TRUE)
#modelTable <- read_csv("/Users/jennamillin/repos/cs600/comp-millinj2/modelTable.csv", "\t", escape_double = FALSE, trim_ws = TRUE)
modelTable$date <- as.Date(modelTable$date, '%m/%d/%Y')
View(modelTable)

stockTable <- read_csv("/Users/jennamillin/repos/cs600/comp-millinj2/stocksTable.csv")
stockTable$dt <- as.Date(stockTable$dt, '%m/%d/%Y')

##########################################################################################

amazonSent = filter(modelTable, company == "Amazon")
amazonSent$sentiment = as.numeric(amazonSent$sentiment)
#amazonSent$sentiment = amazonSent$sentiment*10
amazon = filter(stockTable, stock == "Amazon")
#amazon$stockValue = as.integer(amazon$stockValue)

#plot the stock value for Amazon
Am_stock <- ggplot(data = amazon, mapping = aes(x = dt, y = stockValue)) + geom_path(aes(colour = "Stock Value")) # + geom_smooth(method = "lm", se = FALSE, color = "black")
Am_stock <- Am_stock + labs(#title = "Amazon Stock",
                            y = "Stock Value",
                            x = "Date",
                            colour = "Legend") 
#sent <- sent + theme(plot.title = element_text(hjust = 0.5))
Am_stock <- Am_stock + scale_color_manual(labels = c("Stock Value", "Average"), values = c("blue", "black")) + guides(color=guide_legend("Legend")) + theme(legend.position = c(0.3, 0.9))
Am_stock

#plot the sentiment scores for Amazon News Articles retrieved
Am_sent <- ggplot(data = amazonSent, mapping = aes(x = dt, y = sentiment)) + geom_point(aes(colour = "Sentiment")) #+ geom_smooth(method = "lm", se = FALSE, color = "black")
Am_sent <- Am_sent + labs(#title = "Amazon News Sentiment",
                    y = "Sentiment Score",
                    x = "Date",
                    colour = "Legend") 
#sent <- sent + theme(plot.title = element_text(hjust = 0.5))
Am_sent <- Am_sent + scale_color_manual(labels = c("Sentiment Path", "Average"), values = c("blue", "black")) + guides(color=guide_legend("Legend")) + theme(legend.position = c(0.3, 0.9))
Am_sent

##########################################################################################

#filter out apple info
appleSent = filter(modelTable, company == "Apple")
appleSent$sentiment = as.numeric(appleSent$sentiment)
apple = filter(stockTable, stock == "Apple")

#plot the stock value for Apple
Ap_stock <- ggplot(data = apple, mapping = aes(x = dt, y = stockValue)) + geom_path(aes(colour = "Stock Value")) #+ geom_smooth(method = "lm", se = FALSE, color = "black")
Ap_stock <- Ap_stock + labs(#title = "Apple Stock",
                          y = "Stock Value",
                          x = "Date",
                          colour = "Legend") 
#sent <- sent + theme(plot.title = element_text(hjust = 0.5))
Ap_stock <- Ap_stock + scale_color_manual(labels = c("Stock Value", "Average"), values = c("blue", "black")) + guides(color=guide_legend("Legend")) + theme(legend.position = c(0.3, 0.9))
Ap_stock

#plot the sentiment scores for Apple News Articles retrieved
Ap_sent <- ggplot(data = appleSent, mapping = aes(x = dt, y = sentiment)) + geom_line(aes(colour = "Sentiment")) #+ geom_smooth(method = "lm", se = FALSE, color = "black")
Ap_sent <- Ap_sent + labs(#title = "Apple News Sentiment",
  y = "Sentiment Score",
  x = "Date",
  colour = "Legend") 
#sent <- sent + theme(plot.title = element_text(hjust = 0.5))
Ap_sent <- Ap_sent + scale_color_manual(labels = c("Sentiment Path", "Average"), values = c("blue", "black")) + guides(color=guide_legend("Legend")) + theme(legend.position = c(0.3, 0.9))
Ap_sent

##########################################################################################

#filter out Google info
googleSent = filter(modelTable, company == "Google")
googleSent$sentiment = as.numeric(googleSent$sentiment)
google = filter(stockTable, stock == "Google")

#plot the stock value for Google
Go_stock <- ggplot(data = google, mapping = aes(x = dt, y = stockValue)) + geom_path(aes(colour = "Stock Value")) #+ geom_smooth(method = "lm", se = FALSE, color = "black")
Go_stock <- Go_stock + labs(#title = "Google Stock",
  y = "Stock Value",
  x = "Date",
  colour = "Legend") 
#sent <- sent + theme(plot.title = element_text(hjust = 0.5))
Go_stock <- Go_stock + scale_color_manual(labels = c("Stock Value", "Average"), values = c("blue", "black")) + guides(color=guide_legend("Legend")) + theme(legend.position = c(0.3, 0.9))
Go_stock

#plot the sentiment scores for Google News Articles retrieved
Go_sent <- ggplot(data = googleSent, mapping = aes(x = dt, y = sentiment)) + geom_line(aes(colour = "Sentiment")) #+ geom_smooth(method = "lm", se = FALSE, color = "black")
Go_sent <- Go_sent + labs(#title = "Google News Sentiment",
  y = "Sentiment Score",
  x = "Date",
  colour = "Legend") 
#sent <- sent + theme(plot.title = element_text(hjust = 0.5))
Go_sent <- Go_sent + scale_color_manual(labels = c("Sentiment Path", "Average"), values = c("blue", "black")) + guides(color=guide_legend("Legend")) + theme(legend.position = c(0.3, 0.9))
Go_sent

##########################################################################################

#filter out IBM info
ibmSent = filter(modelTable, company == "IBM")
ibmSent$sentiment = as.numeric(obmSent$sentiment)
ibm = filter(stockTable, stock == "IBM")

#plot the stock value for IBM
Ib_stock <- ggplot(data = ibm, mapping = aes(x = dt, y = stockValue)) + geom_path(aes(colour = "Stock Value")) #+ geom_smooth(method = "lm", se = FALSE, color = "black")
Ib_stock <- Ib_stock + labs(#title = "IBM Stock",
  y = "Stock Value",
  x = "Date",
  colour = "Legend") 
#sent <- sent + theme(plot.title = element_text(hjust = 0.5))
Ib_stock <- Ib_stock + scale_color_manual(labels = c("Stock Value", "Average"), values = c("blue", "black")) + guides(color=guide_legend("Legend")) + theme(legend.position = c(0.3, 0.9))
Ib_stock

#plot the sentiment scores for IBM News Articles retrieved
Ib_sent <- ggplot(data = ibmSent, mapping = aes(x = dt, y = sentiment)) + geom_line(aes(colour = "Sentiment")) #+ geom_smooth(method = "lm", se = FALSE, color = "black")
Ib_sent <- Ib_sent + labs(#title = "IBM News Sentiment",
  y = "Sentiment Score",
  x = "Date",
  colour = "Legend") 
#sent <- sent + theme(plot.title = element_text(hjust = 0.5))
Ib_sent <- Ib_sent + scale_color_manual(labels = c("Sentiment Path", "Average"), values = c("blue", "black")) + guides(color=guide_legend("Legend")) + theme(legend.position = c(0.3, 0.9))
Ib_sent

##########################################################################################

#filter out intel info
intelSent = filter(modelTable, company == "Intel")
intelSent$sentiment = as.numeric(intelSent$sentiment)
intel = filter(stockTable, stock == "Intel")

#plot the stock value for Intel
In_stock <- ggplot(data = intel, mapping = aes(x = dt, y = stockValue)) + geom_path(aes(colour = "Stock Value")) #+ geom_smooth(method = "lm", se = FALSE, color = "black")
In_stock <- In_stock + labs(#title = "Intel Stock",
  y = "Stock Value",
  x = "Date",
  colour = "Legend") 
#sent <- sent + theme(plot.title = element_text(hjust = 0.5))
In_stock <- In_stock + scale_color_manual(labels = c("Stock Value", "Average"), values = c("blue", "black")) + guides(color=guide_legend("Legend")) + theme(legend.position = c(0.3, 0.9))
In_stock

#plot the sentiment scores for Intel News Articles retrieved
In_sent <- ggplot(data = intelSent, mapping = aes(x = dt, y = sentiment)) + geom_line(aes(colour = "Sentiment")) #+ geom_smooth(method = "lm", se = FALSE, color = "black")
In_sent <- In_sent + labs(#title = "Intel News Sentiment",
  y = "Sentiment Score",
  x = "Date",
  colour = "Legend") 
#sent <- sent + theme(plot.title = element_text(hjust = 0.5))
In_sent <- In_sent + scale_color_manual(labels = c("Sentiment Path", "Average"), values = c("blue", "black")) + guides(color=guide_legend("Legend")) + theme(legend.position = c(0.3, 0.9))
In_sent

##########################################################################################

#filter out microsoft info
microSent = filter(modelTable, company == "Microsoft")
microSent$sentiment = as.numeric(microSent$sentiment)
microSent$date = as.Date(microSent$date)
micro = filter(stockTable, stock == "Microsoft")

#plot the stock value for Microsoft
Mi_stock <- ggplot(data = micro, mapping = aes(x = dt, y = stockValue)) + geom_path(aes(colour = "Stock Value")) #+ geom_smooth(method = "lm", se = FALSE, color = "black")
Mi_stock <- Mi_stock + labs(#title = "Microsoft Stock",
  y = "Stock Value",
  x = "Date",
  colour = "Legend") 
#sent <- sent + theme(plot.title = element_text(hjust = 0.5))
Mi_stock <- Mi_stock + scale_color_manual(labels = c("Stock Value", "Average"), values = c("blue", "black")) + guides(color=guide_legend("Legend")) + theme(legend.position = c(0.3, 0.9))
Mi_stock

#plot the sentiment scores for Microsoft News Articles retrieved
Mi_sent <- ggplot(data = microSent, mapping = aes(x = date, y = sentiment)) + geom_line(aes(colour = "Sentiment")) #+ geom_smooth(method = "lm", se = FALSE, color = "black")
Mi_sent <- Mi_sent + labs(#title = "Microsoft News Sentiment",
  y = "Sentiment Score",
  x = "Date",
  colour = "Legend") 
#sent <- sent + theme(plot.title = element_text(hjust = 0.5))
Mi_sent <- Mi_sent + scale_color_manual(labels = c("Sentiment Path", "Average"), values = c("blue", "black")) + guides(color=guide_legend("Legend")) + theme(legend.position = c(0.3, 0.9))
Mi_sent

##########################################################################################

a <- c(modelTable$keywords)
a <- tolower(a)
a <- removePunctuation(a)
a <- removeNumbers(a)
freq_terms(a)

View(a)
