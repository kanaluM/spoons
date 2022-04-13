from sources.Player import Player
from sources.Decks import Decks

class Game(object):
    "Spoon game model"
    
    def __init__(self, player_strategy = ["GREEDY"]*4):
        self.player_strategy = player_strategy
        self.history = [0]*len(player_strategy)

    def initialize_game(self):
        self.deck = Decks()    
        self.player_list = [Player(strat) for strat in self.player_strategy]

        for idx in range(4):
            for player in self.player_list:
                player.add_card(self.deck.next_card())

    def play(self) -> int: 
        MAX_NUMBER_TURNS = 1_000_000
        for n in range(MAX_NUMBER_TURNS):
            if self.check_winner():
                self.history[self.get_winner()] += 1
                break

            next_card = self.deck.next_card()
            for idx, player in enumerate(self.player_list):
                next_card = player.move(next_card)

            self.deck.update_discard_pile(next_card)

    def check_winner(self) -> bool:
        for idx, player in enumerate(self.player_list):
            if player.win():
                return True
        return False
            
    def get_winner(self) -> int:
        for idx, player in enumerate(self.player_list):
            if player.win():
                return idx
        print("invalid use of the function get_winner")
        return -1
        