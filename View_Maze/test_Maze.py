#view the maze from csv

#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

import os
import pytest
from View_Maze import *


#1 Passing Test Case

#User inpuit to view the maze
def test_viewMaze():
    viewmaze = read_csv()
    assert viewmaze == "Success to view Maze"

    
#2 Passing Test Case

#User exit the page
def test_exitpage():
    exits = read_csv()
    assert exits == "Exits from page"


#2 Failing Test Case

    #User is able to view maze without input file inserted
def test_noInput():
    noinput = read_csv()
    assert noinput == "No input file was inserted"


