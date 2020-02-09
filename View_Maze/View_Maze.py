import sys
import csv
import time

def read_csv():
   # print(fileoutput)

    file_directory = "maze.csv"
    with open(file_directory,'rt') as csvfile:

        spamreader = csv.reader(csvfile)
        for row in spamreader:
            #print(', '.join(row))
            print(row)
    #menu()
    return "Success to view Maze"
#read_csv()
        



