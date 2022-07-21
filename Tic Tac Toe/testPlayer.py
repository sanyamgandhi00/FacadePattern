
import pytest
from cell import Cell
from board import Board 
from player import Player



def test_Cell1():
    p1 = Player("Sanyam" , 'X')
    b = Board()
    return p1.markCell(b , 0 , 0 ) == True


def test_Cell2():
    p1 = Player("Sanyam" , 'X')
    b = Board()
    p1.markCell(b , 0 , 0 )
    return p1.markCell(b , 0 , 0 ) == False