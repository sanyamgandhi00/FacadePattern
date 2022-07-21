import random 
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = (2,3,4,5,6,7,8,9,10 , 'J', 'Q', 'K', 'A')

class Card:
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
        