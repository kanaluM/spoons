#import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

class Game_History(object):
    SNAPSHOT_RATE = 50
    
    def __init__(self, player_strategy):
        self.player_strategy = player_strategy
        self.game_history = [0]*len(player_strategy)
        self.wins = []
        self.turns = []
        
    def update(self, winner_id, turns):
        self.game_history[winner_id] += 1
        self.turns += [turns]
        
        if sum(self.game_history) % self.SNAPSHOT_RATE == 0:
            self.wins.append(list(map(lambda x: x/sum(self.game_history), 
                                          self.game_history)))
            
    def win_rates_over_time(self):
        column_names = []
        for idx, player_strat in enumerate(self.player_strategy):
            column_names.append(f"Player {idx + 1}:{player_strat}")
       
        df = pd.DataFrame(self.wins, columns = column_names)
        df.index *= self.SNAPSHOT_RATE
        df.plot(xlabel = "# of games", ylabel = "Winrate (%)")
        return df

    def plotTurns(self):
        plt.hist(self.turns, bins=20, facecolor='g', alpha=0.75)
        plt.xlabel('Turns')
        plt.ylabel('Frequency')
        plt.title('Turns per Game')
        print(f"Min # of turns: {min(self.turns)}\nMax # of turns: {max(self.turns)}\nAverage # of turns: {sum(self.turns)/len(self.turns)}")
        plt.show()