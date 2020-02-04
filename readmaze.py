import xlrd
import numpy as np
import pandas as pd

def load_file(filename):
    f = filename
    sList = f.split('.')

    if (len(sList) != 2):
        print ("Error, please try again")

    else:
        name = sList[0]
        ext = sList[1]
        #If extension is anything other than a csv, display Error
        if ((name != "maze") and (ext != "csv")):
            print ("Error, file could not be found!")
        elif (ext != "csv"):
            print ("Error, please ensure the extension is correct")
        elif (name != "maze"):
            print ("File could not be found!")
        
        else:
            print ("Loading file...")
            file_name = "C:/Users/rayne/Desktop/Np Stuff/Year 3.2/Emerging Trends in IT/maze.csv"
            sheet =  "maze"

            
            data = pd.read_csv(file_name, header=None)
            print (data)

def main():
    value = input("Enter the name of the datafile:")
    load_file(value)


main()