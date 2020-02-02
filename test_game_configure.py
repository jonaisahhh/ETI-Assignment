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

#User inpuit the correct options to configure .csv file
def test_CorrectInput():
    filenameToLoad = 'maze.csv'
    #Call the function to load csv
    user_input = '4'
    #User input to configure current loaded csv
    user_config_input = '2'
    #User configuration option input to configure current loaded csv
    user_coordinate_configure = '3,3'
    #User enters coordinates of the item to configure on the csv file
    user_exit_input = 'M'
    assert trytoload == 'Success'
#2 Failing Test Case

#User tries the input with no file loaded
def test_NofileLoaded():
    filenameToLoad = ''
    #Call function to load csv with filenameToLoad
    user_input = '4'
    assert trytoload == 'File could not be found'

#User input an invalid coordinate
def test_InvalidCoordinates():
    filenameToLoad = 'maze.csv'
    #Call function to load csv with filenameToLoad
    user_input = '4'
    #User input to configure current loaded csv
    user_config_input = '2'
    #User configuration option input to configure current loaded csv
    user_coordinate_configure = '69,69'
    #User enters coordinates of the item to configure on the csv file
    assert trytoload == 'Error!'
