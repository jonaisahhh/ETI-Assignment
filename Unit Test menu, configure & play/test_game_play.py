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

#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import pytest

#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
# Read and load maza from file, this feature allows the application to read the maza diagram from the data file and store it in memory. It also stores the start (A) location and
# the end (B) location. The application should prompt the user for the name of the data file. The number of records/lines read is then displayed
import maze_game

mock = Mock()

from test_imports import *

#1 Passing Test Case

#User inpuit the correct options to view the file
# def test_menu_shows_up():
#     set_keyboard_input(["1","maze4.csv"])
#     maze_game.menu()
#     output = get_display_output()
#     assert output == ["Success","Success"]

def test_CorrectInput():
    maze_game.csvlist = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'O', 'O', 'O', 'X', 'A', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'], ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'], ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]
    #trytoload = maze_game.load_csv("maze4.csv")
    set_keyboard_input(["M", "n"])
    with pytest.raises(SystemExit) as exc:
        maze_game.play_maze("maze4.csv")
        output = get_display_output()
        assert exc.value.code == 1


    # Call the function to load csv


    # output = get_display_output()
    # pytest_wrapped_exit = pytest.raises(SystemExit)

#     assert output == ["""['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
# # ['X', 'O', 'O', 'O', 'X', 'A', 'O', 'X']
# # ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X']
# # ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X']
# # ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X']
# # ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X']
# # ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X']
# # ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']""","Postion of starting point is Row 2 Column: 6","Postion of ending point is Row 8 Column: 2","Goodbye"]



#User test for a completed maze
def test_SuccessfulMazeReachedEnd():
    maze_game.csvlist = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'O', 'O', 'O', 'X', 'O', 'O', 'X'],
                         ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
                         ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
                         ['X', 'A', 'X', 'O', 'O', 'O', 'X', 'X'], ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]
    #trytoload = maze_game.load_csv("maze4.csv")
    set_keyboard_input(["S", "n"])
    with pytest.raises(SystemExit) as exc:
        maze_game.play_maze("maze4.csv")
        output = get_display_output()
        assert exc.value.code == 1

    #Call the function to load csv

    #Check if upon completing maze will a message be displayed
def test_SuccessfulMazeComplete():
    maze_game.csvlist = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                         ['X', 'O', 'O', 'A', 'X', 'O', 'O', 'X'],
                         ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'],
                         ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
                         ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
                         ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
                         ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'],
                         ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]
    #trytoload = maze_game.load_csv("maze4.csv")
    set_keyboard_input(["A", "D","S","W","A","A","S","S","S","S","S","S","n"])
    with pytest.raises(SystemExit) as exc:
        maze_game.play_maze("maze4.csv")
        output = get_display_output()
        assert exc.value.code == 1

    #Call the function to load csv

    #Check if upon completing maze will a message be displayed



    
#2 Failing Test Case

#User tries the input with no file loaded
def test_NofileLoaded():
    filenameToLoad = ''
    #Call function to load csv with filenameToLoad
    set_keyboard_input(["n"])
    with pytest.raises(SystemExit) as exc:
        maze_game.play_maze("")
        output = get_display_output()
        assert exc.value.code == 1
    #fail = maze_game.play_maze("")

    #assert fail == 'File could not be found'

#User input an invalid move
def test_Invalidmove():
    maze_game.csvlist = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'O', 'O', 'O', 'X', 'O', 'O', 'X'],
                         ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
                         ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
                         ['X', 'A', 'X', 'O', 'O', 'O', 'X', 'X'], ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]
    # trytoload = maze_game.load_csv("maze4.csv")
    set_keyboard_input(["D"])
    with pytest.raises(IndexError) as exc:
        maze_game.play_maze("maze4.csv")
        output = get_display_output()
        assert exc.value.code == 1

    #maze_game.movement = lambda: 'D'
    #assert output == get_display_output()


#User inputs invalid movement keys not WASD
#def test_InvalidMoveInput():

##Still somewhat psuedo code
def test_DifferentMoveKey():
    maze_game.csvlist = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'O', 'O', 'O', 'X', 'O', 'O', 'X'],
                         ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
                         ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
                         ['X', 'A', 'X', 'O', 'O', 'O', 'X', 'X'], ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]
    # trytoload = maze_game.load_csv("maze4.csv")
    set_keyboard_input(["F"])
    with pytest.raises(IndexError) as exc:
        maze_game.play_maze("maze4.csv")
        output = get_display_output()
        assert exc.value.code == 1