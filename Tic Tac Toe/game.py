from player import Player
from board import Board

game  = None 

class Game:
    def __init__(self , player1 , player2 , b , turn):
        self.player1 = player1
        self.player2 = player2 
        self.board = b
        self.turn = turn

    @staticmethod
    def createGame(name1 , name2 ):
        global game 
        if game is not None:
            return game 
        
        player1 = Player(name1 , 'X')
        player2 = Player(name2 , 'O')
        b = Board()
        turn = 0
        game = Game(player1 , player2 , b , turn) 
        return game 

    def play(self , row , col):
        while self.board.resultAnalyzer() == "Continue":
            if self.turn % 2 == 0 :
                player = self.player1
            else :
                player  = self.player2 

            row = int(input("Enter Row"))
            col = int(input("Enter Col"))
            
            isMarked  = player.markCell(self.board , row , col) 

            if isMarked == True:
                self.turn +=1
            else :
                print("Cell Already Marked Play again")

            res = self.board.resultAnalyzer()

            if res == "End" :
                print(player , " Wins")
                break 
            elif res == "Draw" : 
                print("Game Draw") 
                break 
            else :
                continue 
                
            


            








game1 = Game()

