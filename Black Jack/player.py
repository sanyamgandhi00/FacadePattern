
from deck import Deck 
import random 

class Player():
    def __init__(self , name ) :
        self.name = name
        self.cardList = [] 
        self.total = 0 
        self.choose = 0
        self.skip = 0 

    def pickACard(self , deck) :
        card = random.choice(deck) 
        if card.rank in range(2,11):
            self.total+=card.rank 
        elif card.rank == 'J':
            self.total+=10 
        elif card.rank == 'Q':
            self.total+=10 
        elif card.rank == 'K':
            self.total+=10 
        else :
            if self.choose == 0:
                inp = int(input("Choose a no from 1 or 11"))
                self.choose = inp 
            self.total += self.choose

        self.cardList.append(card)
        deck.remove(card) 






        
            

