#Load maze game from csv
import os
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import pytest
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
# Read and load maza from file, this feature allows the application to read the maza diagram from the data file and store it in memory. It also stores the start (A) location and
# the end (B) location. The application should prompt the user for the name of the data file. The number of records/lines read is then displayed

#1 Passing Test Case

#User inpuit the correct options to view the file
def test_CorrectInput():
    filenameToLoad = 'maze.csv'
    #Call the function to load csv
    user_input = '3'
    #User input to play current loaded csv
    assert trytoload == 'Success'

def test_SuccessfulMazeComplete():
    filenameToLoad = 'maze.csv'
    #Call the function to load csv
    user_move_input = 'S'
    #User input moves to complete the maze
    assert trytoload == congratz_won()


    
#2 Failing Test Case

#User tries the input with no file loaded
def test_NofileLoaded():
    filenameToLoad = ''
    #Call function to load csv with filenameToLoad
    user_input = '3'
    assert trytoload == 'File could not be found'

#User input an invalid move
def test_Invalidmove():
    filenameToLoad = 'maze.csv'
    #Call function to load csv with filenameToLoad
    user_input = '3'
    #User input to configure current loaded csv
    user_move_input = 'D'
    #User input move to move to the right where there is a wall
    
    assert trytoload == 'Error!'
