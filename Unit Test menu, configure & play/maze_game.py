import sys
import csv
import time

fileoutput = []
csvlist =[]
origin_list = []
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
        return "To be implemented2"
    elif choice == "3" or choice =="3":
        add_into_list()
        play_maze(fileoutput[0])
        return "To be implemented3"
    elif choice=="4" or choice=="4":
        return "To be implemented4"
    elif choice=="0" or choice=="0":
        sys.exit()
    else:
        print("You must only select either 1,2,3,4 or 0.")
        print("Please try again")
        menu()

#Load maze game from csv
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Read and load maza from file, this feature allows the application to read the maza diagram from the data file and store it in memory. It also stores the start (A) location and
# the end (B) location. The application should prompt the user for the name of the data file. The number of records/lines read is then displayed

#1 Passing Test Case

#User inpuit the correct .csv file
def test_CorrectInput():
    trytoload = load_csv("maze.csv")
    #Call the function to load csv, expected return type should be a 1, 1 for success, 0 for fail
    assert trytoload == 1

#2 Failing Test Case

#User input the wrong name
def test_WrongName():
    trytoload = load_csv('msze.csv')
    #Call function to load csv with filenameToLoad
    assert trytoload == 0 #

#User input the wrong extension
def test_WrongExt():
    trytoload = load_csv('maze.doc')
    #Call function to load csv with filenameToLoad
    assert trytoload == 0 # Expect 0 failing




def load_csv(f):
    file = f
    
    if (file == ""):
        print("File not selected")
        print("Number of lines read = 0")
        return "File not selected"

    else:

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
                    return "Success"
                else:
                    fileoutput.append(file)
                    return "Success"
                #Return back to menu 
                menu()
        except FileNotFoundError:
            print("File not found")
            print("Number of lines read:0")
            return "File not found"
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

def add_into_list():
    try:
        with open(fileoutput[0], 'rt') as csvfile:
            csv_reader = csv.reader(csvfile)
            global csvlist
            global origin_list
            #for row in csv_reader:
                #print(', '.join(row))
                #print(row)
            csvfile.seek(0)
            if len(csvlist) >= 1:

                csvlist.clear()
                csvlist = list(csv_reader)
                csvfile.seek(0)
                origin_list = list(csv_reader)
                return 1
            else:
                csvlist = list(csv_reader)
                csvfile.seek(0)
                origin_list = list(csv_reader)
                return 1
    except (IndexError,FileNotFoundError):
        print("File is not found please load a file first")
        return [0,menu()]
        



        #spamreader = csv.reader(csvfile)
        #for row in spamreader:
            # print(', '.join(row))
            #print(row)

def cfm_return_to_menu():
    cfm = input("Return to menu? Y/N")
    if cfm == 'y' or cfm == 'Y':
        return menu()
    elif cfm == 'n' or cfm == 'N':
        print("Goodbye")
        sys.exit()
    else:
        print("Well you didn't press N or Y so out you go")
        sys.exit()


def play_maze(g):
    #fileoutput[0] = g
    #pytest_print()
    try:
        with open(g, 'w+',newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvfile.seek(0)
            writer.writerows(csvlist)
            # way to write to csv file
            #print(csvlist)
            for row in csvlist:
                print(row)
                

            try:
                for sub_list in csvlist:
                    if 'A' in sub_list:
                        row_a = csvlist.index(sub_list)
                        column_a = sub_list.index('A')
                        print("Postion of starting point is Row " + str((csvlist.index(sub_list)+1)) + " Column: " + str((sub_list.index('A')+1)))
                        
            except ValueError:
                print("No such character in list")
                

            try:
                for sub_list in csvlist:
                    if 'B' in sub_list:
                        row_b = csvlist.index(sub_list)
                        column_b = sub_list.index('B')
                        
                        print("Postion of ending point is Row " + str((csvlist.index(sub_list)+1))+ " Column: " + str((sub_list.index('B')+1)))
                        
            except ValueError:
                print("No such character in list")
                
            
        
            #movement = input("Press 'W' for UP, 'A' for LEFT, 'D' for RIGHT & 'S' for DOWN, 'M' for MAIN MENU:")
            try:
                while ((row_a != row_b) & (column_a != column_b)) or ((row_a == row_b) & (column_a != column_b)) or ((row_a != row_b) & (column_a == column_b)):
                    movement = input("Press 'W' for UP, 'A' for LEFT, 'D' for RIGHT & 'S' for DOWN, 'M' for MAIN MENU:")
                    csvfile.seek(0)
                    if (movement == 'D' or movement == 'd') and (csvlist[row_a][column_a + 1] == 'X'):

                        for row in csvlist:
                            print(row)
                        csvfile.seek(0)

                        csvfile.seek(0)
                        try:
                            for sub_list in csvlist:
                                if 'A' in sub_list:
                                    row_a = csvlist.index(sub_list)
                                    column_a = sub_list.index('A')
                                    print("Postion of starting point is Row " + str((csvlist.index(sub_list) + 1)) + " Column: " +
                                          str((sub_list.index('A') + 1)))
                        except ValueError:
                            print("No such character in list")

                        try:
                            for sub_list in csvlist:
                                if 'B' in sub_list:
                                    row_b = csvlist.index(sub_list)
                                    column_b = sub_list.index('B')
                                    print("Postion of ending point is Row " + str((csvlist.index(sub_list) + 1)) + " Column: " +
                                          str((sub_list.index('B') + 1)))
                        except ValueError:
                            print("No such character in list")
                        print("Invalid move, try again")
                        #movement = input("Press 'W' for UP, 'A' for LEFT, 'D' for RIGHT & 'S' for DOWN, 'M' for MAIN MENU:")

                    elif (movement == 'D' or movement == 'd') and (csvlist[row_a][column_a + 1] == 'O' or csvlist[row_a][column_a + 1] == 'B'):

                        try:
                            for sub_list in csvlist:
                                if 'A' in sub_list:
                                    row_a = csvlist.index(sub_list)
                                    column_a = sub_list.index('A')
                                    print("Postion of starting point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('A') + 1)
                        except ValueError:
                            print("No such character in list")

                        try:
                            for sub_list in csvlist:
                                if 'B' in sub_list:
                                    row_b = csvlist.index(sub_list)
                                    column_b = sub_list.index('B')
                                    print("Postion of ending point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('B') + 1)
                        except ValueError:
                            print("No such character in list")
                        csvfile.seek(0)
                        csvlist[row_a][column_a] = 'O'
                        csvlist[row_a][column_a+1] = 'A'
                        writer.writerows(csvlist)
                        csvfile.seek(0)
                        for row in csvlist:
                            print(row)
                        try:
                            for sub_list in csvlist:
                                if 'A' in sub_list:
                                    row_a = csvlist.index(sub_list)
                                    column_a = sub_list.index('A')
                                    print("Postion of starting point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('A') + 1)
                        except ValueError:
                            print("No such character in list")

                        try:
                            for sub_list in csvlist:
                                if 'B' in sub_list:
                                    row_b = csvlist.index(sub_list)
                                    column_b = sub_list.index('B')
                                    print("Postion of ending point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('B') + 1)
                        except ValueError:
                            print("No such character in list")
                        csvfile.seek(0)
                        print("Valid move D")
                        #movement = input("Press 'W' for UP, 'A' for LEFT, 'D' for RIGHT & 'S' for DOWN, 'M' for MAIN MENU:")

                    elif (movement == 'A' or movement == 'a') and (csvlist[row_a][column_a - 1] == 'X'):

                        for row in csvlist:
                            print(row)
                        csvfile.seek(0)

                        csvfile.seek(0)
                        try:
                            for sub_list in csvlist:
                                if 'A' in sub_list:
                                    row_a = csvlist.index(sub_list)
                                    column_a = sub_list.index('A')
                                    print("Postion of starting point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('A') + 1)
                        except ValueError:
                            print("No such character in list")

                        try:
                            for sub_list in csvlist:
                                if 'B' in sub_list:
                                    row_b = csvlist.index(sub_list)
                                    column_b = sub_list.index('B')
                                    print("Postion of ending point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('B') + 1)
                        except ValueError:
                            print("No such character in list")
                        print("Invalid move, try again")
                        #movement = input("Press 'W' for UP, 'A' for LEFT, 'D' for RIGHT & 'S' for DOWN, 'M' for MAIN MENU:")
                    elif (movement == 'A' or movement == 'a') and (csvlist[row_a][column_a - 1] == 'O' or csvlist[row_a][column_a - 1] == 'B'):
                        try:
                            for sub_list in csvlist:
                                if 'A' in sub_list:
                                    row_a = csvlist.index(sub_list)
                                    column_a = sub_list.index('A')
                                    print("Postion of starting point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('A') + 1)
                        except ValueError:
                            print("No such character in list")

                        try:
                            for sub_list in csvlist:
                                if 'B' in sub_list:
                                    row_b = csvlist.index(sub_list)
                                    column_b = sub_list.index('B')
                                    print("Postion of ending point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('B') + 1)
                        except ValueError:
                            print("No such character in list")
                        csvfile.seek(0)
                        csvlist[row_a][column_a] = 'O'
                        csvlist[row_a][column_a-1] = 'A'
                        writer.writerows(csvlist)
                        csvfile.seek(0)
                        for row in csvlist:
                            print(row)
                        try:
                            for sub_list in csvlist:
                                if 'A' in sub_list:
                                    row_a = csvlist.index(sub_list)
                                    column_a = sub_list.index('A')
                                    print("Postion of starting point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('A') + 1)
                        except ValueError:
                            print("No such character in list")

                        try:
                            for sub_list in csvlist:
                                if 'B' in sub_list:
                                    row_b = csvlist.index(sub_list)
                                    column_b = sub_list.index('B')
                                    print("Postion of ending point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('B') + 1)
                        except ValueError:
                            print("No such character in list")
                        print("Valid move A")
                        #movement = input("Press 'W' for UP, 'A' for LEFT, 'D' for RIGHT & 'S' for DOWN, 'M' for MAIN MENU:")

                    elif (movement == 'W' or movement == 'w') and (csvlist[row_a-1][column_a] == 'O' or csvlist[row_a-1][column_a] == 'B'):

                        try:
                            for sub_list in csvlist:
                                if 'A' in sub_list:
                                    row_a = csvlist.index(sub_list)
                                    column_a = sub_list.index('A')
                                    print("Postion of starting point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('A') + 1)
                        except ValueError:
                            print("No such character in list")

                        try:
                            for sub_list in csvlist:
                                if 'B' in sub_list:
                                    row_b = csvlist.index(sub_list)
                                    column_b = sub_list.index('B')
                                    print("Postion of ending point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('B') + 1)
                        except ValueError:
                            print("No such character in list")
                        csvfile.seek(0)
                        csvlist[row_a][column_a] = 'O'
                        csvfile.seek(0)
                        csvlist[row_a-1][column_a] = 'A'
                        writer.writerows(csvlist)
                        csvfile.seek(0)
                        for row in csvlist:
                            print(row)
                        try:
                            for sub_list in csvlist:
                                if 'A' in sub_list:
                                    row_a = csvlist.index(sub_list)
                                    column_a = sub_list.index('A')
                                    print("Postion of starting point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('A') + 1)
                        except ValueError:
                            print("No such character in list")

                        try:
                            for sub_list in csvlist:
                                if 'B' in sub_list:
                                    row_b = csvlist.index(sub_list)
                                    column_b = sub_list.index('B')
                                    print("Postion of ending point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('B') + 1)
                        except ValueError:
                            print("No such character in list")
                        print("Valid move W")
                        #movement = input("Press 'W' for UP, 'A' for LEFT, 'D' for RIGHT & 'S' for DOWN, 'M' for MAIN MENU:")
                    elif movement == 'M' or movement == 'm':
    ##                    try:
    ##                        for sub_list in csvlist:
    ##                            if 'A' in sub_list:
    ##                                row_a = csvlist.index(sub_list)
    ##                                column_a = sub_list.index('A')
    ##                                print("Postion of starting point is Row " + str((csvlist.index(sub_list) + 1)) + " Column: " +
    ##                                      str((sub_list.index('A') + 1)))
    ##                    except ValueError:
    ##                        print("No such character in list")
    ##
    ##                    try:
    ##                        for sub_list in csvlist:
    ##                            if 'B' in sub_list:
    ##                                row_b = csvlist.index(sub_list)
    ##                                column_b = sub_list.index('B')
    ##                                print("Postion of ending point is Row " + str((csvlist.index(sub_list) + 1)) + " Column: " +
    ##                                      str((sub_list.index('B') + 1)))
    ##                    except ValueError:
    ##                        print("No such character in list")
                        print("Exiting current maze")

                        csvfile.seek(0)
                        writer.writerows(csvlist)
                        cfm_return_to_menu()

                    elif (movement == 'S' or movement == 's') and (csvlist[row_a+1][column_a] == 'O' or csvlist[row_a+1][column_a] == 'B'):

                        try:
                            for sub_list in csvlist:
                                if 'A' in sub_list:
                                    row_a = csvlist.index(sub_list)
                                    column_a = sub_list.index('A')
                                    print("Postion of starting point is Row " + str((csvlist.index(sub_list) + 1)) + " Column: " +
                                          str((sub_list.index('A') + 1)))
                        except ValueError:
                            print("No such character in list")

                        try:
                            for sub_list in csvlist:
                                if 'B' in sub_list:
                                    row_b = csvlist.index(sub_list)
                                    column_b = sub_list.index('B')
                                    print("Postion of ending point is Row " + str((csvlist.index(sub_list) + 1)) + " Column: " +
                                          str((sub_list.index('B') + 1)))
                        except ValueError:
                            print("No such character in list")
                        csvfile.seek(0)
                        csvlist[row_a][column_a] = 'O'
                        csvlist[row_a+1][column_a] = 'A'
                        writer.writerows(csvlist)
                        csvfile.seek(0)
                        for row in csvlist:
                            print(row)
                        try:
                            for sub_list in csvlist:
                                if 'A' in sub_list:
                                    row_a = csvlist.index(sub_list)
                                    column_a = sub_list.index('A')
                                    print("Postion of starting point is Row " + str((csvlist.index(sub_list) + 1)) + " Column: " +
                                          str((sub_list.index('A') + 1)))
                        except ValueError:
                            print("No such character in list")

                        try:
                            for sub_list in csvlist:
                                if 'B' in sub_list:
                                    row_b = csvlist.index(sub_list)
                                    column_b = sub_list.index('B')
                                    print("Postion of ending point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('B') + 1)
                        except ValueError:
                            print("No such character in list")
                        print("Valid move S")
                        #movement = input("Press 'W' for UP, 'A' for LEFT, 'D' for RIGHT & 'S' for DOWN, 'M' for MAIN MENU:")

                    elif (movement == 'S' or movement == 's') and (csvlist[row_a+1][column_a] == 'X'):
                        for row in csvlist:
                            print(row)
                        csvfile.seek(0)

                        csvfile.seek(0)
                        try:
                            for sub_list in csvlist:
                                if 'A' in sub_list:
                                    row_a = csvlist.index(sub_list)
                                    column_a = sub_list.index('A')
                                    print("Postion of starting point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('A') + 1)
                        except ValueError:
                            print("No such character in list")

                        try:
                            for sub_list in csvlist:
                                if 'B' in sub_list:
                                    row_b = csvlist.index(sub_list)
                                    column_b = sub_list.index('B')
                                    print("Postion of ending point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('B') + 1)
                        except ValueError:
                            print("No such character in list")
                        print("Invalid move, try again")
                        #movement = input("Press 'W' for UP, 'A' for LEFT, 'D' for RIGHT & 'S' for DOWN, 'M' for MAIN MENU:")

                    elif (movement == 'W' or movement == 'w') and (csvlist[row_a-1][column_a] == 'X'):
                        for row in csvlist:
                            print(row)
                        csvfile.seek(0)

                        csvfile.seek(0)
                        try:
                            for sub_list in csvlist:
                                if 'A' in sub_list:
                                    row_a = csvlist.index(sub_list)
                                    column_a = sub_list.index('A')
                                    print("Postion of starting point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('A') + 1)
                        except ValueError:
                            print("No such character in list")

                        try:
                            for sub_list in csvlist:
                                if 'B' in sub_list:
                                    row_b = csvlist.index(sub_list)
                                    column_b = sub_list.index('B')
                                    print("Postion of ending point is Row", csvlist.index(sub_list) + 1, "Column:",
                                          sub_list.index('B') + 1)
                        except ValueError:
                            print("No such character in list")
                        print("Invalid move, try again")
                        #movement = input("Press 'W' for UP, 'A' for LEFT, 'D' for RIGHT & 'S' for DOWN, 'M' for MAIN MENU:")
                        return 1
                    else:
                        for row in csvlist:
                            print(row)
                        csvfile.seek(0)

                        csvfile.seek(0)
                        try:
                            for sub_list in csvlist:
                                if 'A' in sub_list:
                                    row_a = csvlist.index(sub_list)
                                    column_a = sub_list.index('A')
                                    print("Postion of starting point is Row " + str((csvlist.index(sub_list) + 1)) + " Column: " +
                                          str((sub_list.index('A') + 1)))
                        except ValueError:
                            print("No such character in list")

                        try:
                            for sub_list in csvlist:
                                if 'B' in sub_list:
                                    row_b = csvlist.index(sub_list)
                                    column_b = sub_list.index('B')
                                    print("Postion of ending point is Row " + str((csvlist.index(sub_list) + 1)) + " Column: " +
                                          str((sub_list.index('B') + 1)))
                        except ValueError:
                            print("No such character in list")
                        print("Invalid move, you can only choose W A S D or M, please try again")

                    
                
                else:
                    print("Congratulations. You have solved the maze")
                    print("Loading ...")
                    csvfile.seek(0)
                    writer.writerows(csvlist)
                    csvfile.seek(0)
                    time.sleep(3)
                    return cfm_return_to_menu()
                    
                    # play_again = input("Would you like to continue? y/n")
                    # if play_again == 'y' or play_again == 'Y':
                    #     print(origin_list)
                    #     writer.writerows(origin_list)
                    #     print("Load the game again from the menu")
                    #     time.sleep(3)
                    #     print(row_b)
                    #     return menu()
                    # elif play_again == 'n' or play_again == 'N':
                    #     print("Thank-you for playing")
                    #     print(row_b)
                    #     time.sleep(2)
                    #     return menu()
                    # else:
                    #     print("You must only select either y or n")
                    #     print("Please try again")
                    #     print(row_b)
                    #     return menu()
            except UnboundLocalError:
                print("This maze is already completed, load a new maze or configure the current one to have an end point to be playable")
                print("Returning to the menu")
                csvfile.seek(0)
                writer.writerows(csvlist)
                csvfile.seek(0)
                time.sleep(3)
                return cfm_return_to_menu()
    except(FileNotFoundError):
        print("File not found test")
        return cfm_return_to_menu()
    return 1



def configure_maze():
    with open(fileoutput[0], 'w+',newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvfile.seek(0)
        writer.writerows(csvlist)
        # way to write to csv file
        for row in csvlist:
            print(row)
        print(
"CONFIGURATION MENU"
"=================="
        )

        print("""
[1]: Create wall
[2]: Create passageway
[3]: Create start point
[4]: Create end point
[0]: Exit to Main menu"""
              )
        config_input = input("Enter your option")
        if config_input == '0':
            print("Return to main menu")
            time.sleep(1)
            menu()
        elif config_input == '1':
            for row in csvlist:
                print(row)
                print("Enter the coordinate you wish to change E.g. Row, Column")
                print("'B' to return to configuration Menu")
                coord_input = input("M to return to Main Menu:")
                if coord_input == 'B' or coord_input =='b':
                    configure_maze()
                elif coord_input == 'M' or coord_input =='m':
                    menu()
                else:
                    d



if __name__ == "__main__":
    menu()
#menu()
