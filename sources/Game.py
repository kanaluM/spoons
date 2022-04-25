from sources.Player import Player
from sources.Decks import Decks
from sources.Game_History import Game_History
import matplotlib.pyplot as plt

class Game(object):
    """
    An object that can be used to simulate a game of spoon
    """
    MAX_NUMBER_TURNS = 1_000_000
 
    def __init__(self, player_strategy = ["GREEDY"]*4):
        self.player_strategy = player_strategy
        self.history = Game_History(self.player_strategy)
        self.turns = 0
        
    def initialize_game(self):
        self.deck = Decks()    
        self.player_list = [Player(strat) for strat in self.player_strategy]

        for idx in range(4):
            for player in self.player_list:
                player.add_card(self.deck.next_card())

    def play(self) -> int: 
        for n in range(self.MAX_NUMBER_TURNS):
            self.turns += 1
            if self.check_winner():
                self.history.update(self.get_winner())
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
    
    def print_game_record(self) -> None:
        self.history.win_rates_over_time()

    def player_freq(self, playerIndex) -> None:
        p = self.player_list[playerIndex]
        xData = list(range(1,self.turns+1))
        yData = p.getFreq()
        plt.plot(xData, yData)
        plt.title("Highest Card Frequency vs Turns")
        plt.xlabel("Turn #")
        plt.ylabel("Highest Current Frequency")
        plt.show()

    def player_unique(self, playerIndex) -> None:
        p = self.player_list[playerIndex]
        xData = list(range(1,self.turns+1))
        yData = p.getUnique()
        plt.plot(xData, yData)
        plt.title("Cards Seen Over Time")
        plt.xlabel("Turn #")
        plt.ylabel("# Cards Seen")
        plt.show()

    