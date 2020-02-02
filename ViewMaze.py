#view the maze from csv
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Read and load maza from file, this feature allows the application to read the maza diagram from the data file and store it in memory. It also stores the start (A) location and
# 


#1 Passing Test Case

#User inpuit to view the maze
def test_viewMaze(): 
    filenameToLoad = 'maze.csv'
    for y in range(self.rowsInMaze):
        for x in range(self.columnsInMaze):
            if self.mazelist[y][x] == OBSTACLE:
                self.drawCenteredBox(x+self.xTranslate,
                                     -y+self.yTranslate,
                                     'tan')
    self.t.color('black','blue')
    
    #Call the function to load csv 
    assert viewmaze == 'Success to view the image'

    
#2 Passing Test Case

#User exit the page
def test_exit page():
    if(show){
    filenameToLoad = 'msze.csv'
    }
    else{
    return (row == 0 or
             row == self.rowsInMaze-1 or
             col == 0 or
             col == self.columnsInMaze-1 )
        }


    #Call function to load csv with filenameToLoad
    assert trytoload == 'System has been exit and display the main menu'



#2 Failing Test Case

    #User is able to view maze without input file inserted
def test_withoutinput():
    if(viewmaze=='')
    {
    filenameToLoad = ''
    }
    
    #Call function to load csv with filenameToLoad
    assert viewmaze == 'File is not selected!'
