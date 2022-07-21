import random
from card import Card 
    
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, \
         'Queen':10, 'King':10, 'Ace':11}

class Deck:
    
    def __init__(self):
        self.deck=[]
        for i in ranks:
            for j in suits:
                self.deck.append(Card(i,j))

    def shuffle(self):
        
        random.shuffle(self.deck)

    def __str__(self):
        for i in self.deck:
            print(f'{i.rank} of {i.suit}')

    def giveCard(self):
        temp=self.deck.pop()
        a=temp.rank
        b= temp.suit
        return a,b

    def showDeck(self):
        for i in self.deck:
            print(f'{i.rank} of {i.suit}')