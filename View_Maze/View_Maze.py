<<<<<<< HEAD
import sys
import csv
import time

def read_csv():
   # print(fileoutput)

    file_directory = "D:\\NgeeAnn\\Year3_Sems_2\\ETI_Module\\Python\\View_Maze\\maze.csv"
    with open(file_directory,'rt') as csvfile:

        spamreader = csv.reader(csvfile)
        for row in spamreader:
            #print(', '.join(row))
            print(row)
    #menu()
    return "Success to view Maze"
#read_csv()
        



=======
import sys
import csv
import time

def read_csv():
   # print(fileoutput)

    file_directory = "D:\\NgeeAnn\\Year3_Sems_2\\ETI_Module\\Python\\View_Maze\\maze.csv"
    with open(file_directory,'rt') as csvfile:

        spamreader = csv.reader(csvfile)
        for row in spamreader:
            #print(', '.join(row))
            print(row)
    #menu()
    return "Success to view Maze"
#read_csv()
        



>>>>>>> 4a9d14f104937644ff02bafb07d47152367b7486
