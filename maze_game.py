import sys
import csv
import time

fileoutput = []
csvlist =[]
def menu():

    print("************MAIN MENU**************")
    #time.sleep(1)
    print(
"""
[1]: Read and load maze from file
[2]: View maze
[3]: Play maze game
[4]: Configure current maze
[0]: Exit Maze
""")
    choice = input("Please enter your choice:")
    if choice == "1" or choice =="1":
        file = input("Enter the name of data file:")
        load_csv(file)
        menu()
    elif choice == "2" or choice =="2":
        read_csv()
        return("To be implemented2")
    elif choice == "3" or choice =="3":
        return("To be implemented3")
    elif choice=="4" or choice=="4":
        return("To be implemented4")
    elif choice=="0" or choice=="0":
        sys.exit
    else:
        print("You must only select either 1,2,3,4 or 0.")
        print("Please try again")
        

def load_csv(f):
    file = f
    
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
        return 0
        load_csv()

def read_csv():
    try:


        with open(fileoutput[0], 'rt') as csvfile:

            spamreader = csv.reader(csvfile)
            for row in spamreader:
                #print(', '.join(row))
                print(row)
        menu()
    except(IndexError,FileNotFoundError):
        print("File is not found please load a file first")
        menu()

menu()
