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
    filenameToLoad = 'maze.csv'
    #Call the function to load csv 
    assert trytoload == 'Success'
#2 Failing Test Case

#User input the wrong name
def test_WrongName():
    filenameToLoad = 'msze.csv'
    #Call function to load csv with filenameToLoad
    assert trytoload == 'File could not be found'

#User input the wrong extension
def test_WrongExt():
    filenameToLoad = 'maze.doc'
    #Call function to load csv with filenameToLoad
    assert trytoload == 'Error!'