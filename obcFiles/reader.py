# loads a datafile of links and processes each one in serial
# load the data file

def openFile2(inFile1):
    #fname = "data.txt"
    #f_list = open(fname,"r").readlines() #each line from the file is a link
    f_list = open(inFile1,"r").readlines() #each line from the file is a link

    #clean each element of list, remove line feeds ("\n")

    data_list = [] #define a list
    for i in f_list:
        tmp = i.replace("\n","")
        data_list.append(tmp)

    print "clean data :",data_list

    return data_list
# end of openFile2() 



def main(): # add to your main method (somehow) 

    inFile1 = "data.txt" # use a parameter from the terminal?
    data_list = openFile2(inFile1) # get a list of the links from the data.txt

    for i in data_list: 
        print i
        url = i
        print " Send this url = ",url," to your newspaper code using a for loop like this..."
# end of mail()

main() # runs the driver method 

