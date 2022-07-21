
import pytest
from board import Board

def testCell1():
    board1 = Board()
    l = board1.printBoard()
    m = ['-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' , ]

    assert l == m



def testCell2():
    board1 = Board()
    board1.board[0][0].mark = 'X'
    l = board1.printBoard()
    m = ['X' , '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' , ]

    assert l == m

def testBoard3():
    board1 = Board()
    assert board1.resultAnalyzer()[0] == False

def testBoard4():
    board1 = Board()
    board1.board[0][0].mark = 'X'
    board1.board[0][1].mark = 'X'
    board1.board[0][2].mark = 'X'
    assert board1.resultAnalyzer()[0] == True


def testBoard4():
    board1 = Board()
    board1.board[0][0].mark = 'O'
    board1.board[0][1].mark = 'O'
    board1.board[0][2].mark = 'O'
    
    assert board1.resultAnalyzer()[0] == True