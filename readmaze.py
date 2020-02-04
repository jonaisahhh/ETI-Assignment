import sys
import csv
import time
fileoutput = []

def load_csv():
    file = input("Enter the name of data file:")

    #Try Catch Block
    try:
        with open(file,'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            row_count=sum(1 for row in csvfile)
            print("Reading",file, "...")
            print("Number of lines read:", row_count)
            if len(fileoutput) >= 1:
                fileoutput.clear()
                fileoutput.append(file)
                return 1
            else:
                fileoutput.append(file)
                return 1
            #Return back to menu 
            menu()
    except FileNotFoundError:
        print(file,"does not exist. Try again")
        load_csv()
        return 0

