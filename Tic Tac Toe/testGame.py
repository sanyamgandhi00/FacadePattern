
import pytest
from game import Game

def test_PlayGame1():
    g = Game.createGame("Sanyam" , "Ayush") 
    g.player1.markCell(0,0)
    g.player2.markCell(1,1)
    g.player1.markCell(0,1)
    g.player2.markCell(1,2)
    ans = g.play(0,2)
    assert  "Sanyam Wins"== ans

def test_PlayGame1():
    g = Game.createGame("Sanyam" , "Ayush") 
    g.player1.markCell(0,0)
    g.player2.markCell(1,1)
    g.player1.markCell(0,1)
    g.player2.markCell(1,2)
    g.player1.markCell(2,2)
    ans = g.play(1,0)
    assert  "Ayush Wins"== ans

def test_PlayGame1():
    g = Game.createGame("Sanyam" , "Ayush") 
    g.player1.markCell(0,0)
    g.player2.markCell(1,1)
    g.player1.markCell(0,1)
    g.player2.markCell(0,2)
    g.player1.markCell(1,2)
    g.player2.markCell(1,0)
    g.player1.markCell(2,2)
    g.player2.markCell(2,0)
    ans = g.play(2,1)
    assert  "Game Draw"== ans
