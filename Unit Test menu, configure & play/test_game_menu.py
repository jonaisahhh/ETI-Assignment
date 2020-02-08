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

#User inpuit the correct options to configure .csv file
def test_CorrectInput():
    user_input = '1'
    #User input to load csv
    user_input = 'maze.csv'
    #User input for csv load
    filenameToLoad = 'maze.csv'
    #Call the function to load csv
    user_input = '2'
    #User input to read currently loaded csv
    filenameToRead = 'maze.csv'
    #CSV file is displayed
    user_input = '3'
    #User input to play currently loaded csv file
    user_movement_input_to_complete_maze = 'W'
    #User inputs movement to complete the maze
    user_input = '4'
    #User input to configure file
    user_redirect = 'Configure file'
    #succesfully redirect to configure file
    assert trytoload == 'Success'
#2 Failing Test Case

#User tries the wrong input
def test_wronginput():
    user_input = '69'
    #Wrong user input
    assert trytoload == 'Out of range, please select input 1,2,3,4 or 0'
