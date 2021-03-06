import sys
import csv
import time
fileoutput = []
#Load maze game from csv
import os

def load_csv(f):
    if (f == ""):
        print("File not selected")
        print("Number of lines read = 0")
        return "File not selected"
    else:
        #Try Catch Block
        try:
            with open(f,'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                row_count=sum(1 for row in csvfile)
                print("Reading",f, "...")
                print("Number of lines read:", row_count)
                if len(fileoutput) >= 1:
                    fileoutput.clear()
                    fileoutput.append(f)
                else:
                    fileoutput.append(f)
                    
                return "Success"
                #Return back to menu 
                menu()
        except FileNotFoundError:
            print("File not found")
            print("Number of lines read:0")
            return "File not found"
            load_csv()

