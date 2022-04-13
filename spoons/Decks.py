import random
from functools import reduce

class Decks(object):
    """A class for a deck of cards"""
    
    def __init__(self):
        self.draw_pile = self.fresh_deck()
        self.shuffle(self.draw_pile)    
        self.discard_pile = []
          
    def __repr__(self):
        return f"Draw pile: {str(self.draw_pile)} \nDiscard pile: {str(self.discard_pile)}"
    
    def fresh_deck(self) -> list:
        return [value for value in range(1, 14)] * 4        

    def shuffle(self, deck) -> None:
        random.shuffle(deck)

    def next_card(self) -> int:
        if self.draw_pile == []:
            self.draw_pile = self.discard_pile
            self.shuffle(self.draw_pile)
            self.discard_pile = []
            
        return self.draw_pile.pop()
        
    def update_discard_pile(self, card_value) -> None:
        self.discard_pile.append(card_value)
    
    
    
