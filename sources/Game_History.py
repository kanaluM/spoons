#import matplotlib.pyplot as plt
import pandas as pd

class Game_History(object):
    SNAPSHOT_RATE = 50
    
    def __init__(self, player_strategy):
        self.player_strategy = player_strategy
        self.game_history = [0]*len(player_strategy)
        self.snapshot = []
        
    def update(self, winner_id):
        self.game_history[winner_id] += 1
        
        if sum(self.game_history) % self.SNAPSHOT_RATE == 0:
            self.snapshot.append(list(map(lambda x: x/sum(self.game_history), 
                                          self.game_history)))
            
    def win_rates_over_time(self):
        column_names = []
        for idx, player_strat in enumerate(self.player_strategy):
            column_names.append(f"Player {idx + 1}:{player_strat}")
       
        df = pd.DataFrame(self.snapshot, columns = column_names)
        df.index *= self.SNAPSHOT_RATE
        df.plot(xlabel = "# of games", ylabel = "Winrate (%)")
        return df