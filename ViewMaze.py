import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#1 Passing Test Case

#User inpuit to view the maze
def test_viewMaze():
    Fileoutput.append("maze.csv")
    #Call the function to load csv 
    assert viewmaze == 'Success to view the image'

    
#2 Passing Test Case

#User exit the page
def test_exitpage():
    try:
        Fileoutput.append("maze.csv")
    finally:
        fileoutput.close()
    #Call function to load csv with filenameToLoad
    assert viewmaze == 'System has been exit and display the main menu'



#2 Failing Test Case

    #User is able to view maze without input file inserted
def test_withoutinput():
    Fileoutput.append("")
    #Call function to load csv with filenameToLoad
    assert viewmaze == 'File is not selected!'


