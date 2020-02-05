import sys
import csv
import time

def read_csv():
    #print(fileoutput)

    file_directory = "D:\\NgeeAnn\\Year3_Sems_2\\ETI_Module\\Python\\maze.csv"
    with open(file_directory,'rt') as csvfile:

        spamreader = csv.reader(csvfile)
        for row in spamreader:
            #print(', '.join(row))
            print(row)
    #menu()
read_csv()


