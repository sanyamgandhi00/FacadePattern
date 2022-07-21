
import pytest
from cell import Cell

def test_Cell1():
    cell1 = Cell()
    cell1.mark = 'X'
    assert cell1.isMarked() == True

def test_Cell2():
    cell1 = Cell()
    cell1.mark = 'O'
    assert cell1.isMarked() == True


def test_Cell3():
    cell1 = Cell()
    cell1.mark = '-'
    assert cell1.isMarked() == False


def test_Cell4():
    cell1 = Cell()
    cell1.mark = 'sduhsf'
    assert cell1.isMarked() == False

