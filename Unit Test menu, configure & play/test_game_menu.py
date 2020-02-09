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

#User inpuit the correct options to configure .csv file
def test_CorrectInput1():
    set_keyboard_input(["1", "maze4.csv","0"])
    with pytest.raises(SystemExit) as exc:
        maze_game.menu()
        output = get_display_output()
        assert exc.value.code == 1

def test_CorrectInput2():
    set_keyboard_input(["2","0"])
    with pytest.raises(SystemExit) as exc:
        maze_game.menu()
        output = get_display_output()
        assert exc.value.code == 1

def test_CorrectInput3():
    maze_game.csvlist = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'O', 'O', 'O', 'X', 'O', 'O', 'X'],
                         ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
                         ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'], ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
                         ['X', 'A', 'X', 'O', 'O', 'O', 'X', 'X'], ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]
    set_keyboard_input(["3", "S","n"])
    #with pytest.raises(SystemExit) as exc:
    with pytest.raises(SystemExit) as exc:
        maze_game.menu()
        output = get_display_output()
        assert exc.value.code == 1
    #assert exc.value.code == 1
def test_CorrectInput4():
    set_keyboard_input(["4"])

    results = maze_game.menu()

    assert results == "To be implemented4"
def test_CorrectInput0():
    set_keyboard_input(["0"])
    with pytest.raises(SystemExit) as exc:
        maze_game.menu()
        output = get_display_output()
        assert exc.value.code == 1
#2 Failing Test Case

#User tries the wrong input
def test_wronginput():
    set_keyboard_input(["69"])
    with pytest.raises(IndexError) as exc:
        maze_game.menu()
        output = get_display_output()
        assert exc.value.code == 1
def test_wronginput1():
    set_keyboard_input([""])
    with pytest.raises(IndexError) as exc:
        maze_game.menu()
        output = get_display_output()
        assert exc.value.code == 1
def test_wronginput1():
    set_keyboard_input(["A"])
    with pytest.raises(IndexError) as exc:
        maze_game.menu()
        output = get_display_output()
        assert exc.value.code == 1
