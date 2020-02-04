import sys
import csv
import time

def read_csv():
    print(fileoutput)

    with open("fileoutput[0]", 'rt') as csvfile:

        spamreader = csv.reader(csvfile)
        for row in spamreader:
            #print(', '.join(row))
            print(row)
    #menu()
    read_csv()


