
from board import Board 

class Player():
    def __init__(self , name , symbol) :
        self.name = name
        self.symbol = symbol 

    def markCell(self , b , row , col) :
        
        if b.board[row][col] != '-' :
            b.board[row][col] = self.symbol 
            return True
        else :
            return False 
            

