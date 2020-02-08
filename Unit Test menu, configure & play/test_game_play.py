#Load maze game from csv
import os
import unittest
from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock
from sys import stderr
from sys import stdout
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import pytest
from _pytest.compat import CaptureIO
from _pytest.fixtures import FixtureRequest
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
# Read and load maza from file, this feature allows the application to read the maza diagram from the data file and store it in memory. It also stores the start (A) location and
# the end (B) location. The application should prompt the user for the name of the data file. The number of records/lines read is then displayed
import maze_game
mock = Mock()
#1 Passing Test Case

#User inpuit the correct options to view the file
def test_CorrectInput(capsys):
    maze_game.csvlist = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'O', 'O', 'O', 'X', 'A', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'], ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]
    #trytoload = maze_game.load_csv("maze4.csv")


    # Call the function to load csv
    out, err = capsys.readouterr()




    loadcsv = maze_game.play_maze("maze4.csv")

    assert maze_game.pytest_print() == 3


    # User input to play current loaded csv
    assert loadcsv == 1




#User test for a completed maze
def test_SuccessfulMazeComplete():
    trytoload = maze_game.load_csv("maze4.csv")
    #Call the function to load csv
    loadcsv = maze_game.play_maze("maze4.csv")
    #Check if upon completing maze will a message be displayed
    assert loadcsv == 0


    
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

#User inputs invalid movement keys not WASD
#def test_InvalidMoveInput():
    
