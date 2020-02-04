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
        return("To be implemented1")
    elif choice == "2" or choice =="2":
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
        



menu()
