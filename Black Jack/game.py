from player import Player 
from deck import Deck 


class Game():
    def __init__(self , deck , player1 , player2) :
        self.deck = deck 
        self.player1 = player1 
        self.player2 = player2 

    @staticmethod
    def startGame(name1 , name2):
        player1 = Player(name1) 
        player2 = Player(name2)
        deck = Deck() 
        return Game(deck , player1 , player2) 

    def play(self , deck ) :
        self.player1.pickACard(deck) 
        self.player1.pickACard(deck) 
        flag = True 
        skipped = True 
        while self.player1.total <= 21 and self.player2.total <= 21:    
            self.player1.pickACard(deck) 
            if self.player1.skip == 1 and self.player2.skip == 1 :
                skipped = False
                return
            if self.player1.total == 21 :
                print(self.player1.name , " Wins")
                flag = False
                break 
            self.player1.pickACard(deck)
            if self.player2.total == 21 :
                print(self.player2.name , " Wins")
                flag = False
                break 
        if skipped:
            if self.player1.total > self.player2.total  :
                print(self.player1.name , " Wins")
            elif  self.player1.total < self.player2.total  :
                print(self.player2.name , " Wins")
            else : 
                print('Draw')
                

        if flag :
            if self.player1.total > 21 :
                print(self.player2.name , " Wins") 
            else :
                print(self.player1.name , " Wins")





        

