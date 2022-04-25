# -*- coding: utf-8 -*-
import random
from sources.Player import Player
from sources.Decks import Decks
from sources.Game import Game

random.seed(42)
NUM_SIMULATION = 2_500

game = Game(["GREEDY_SIMPLE"]*2+["GREEDY_HIST_RAND"]*2)
for n in range(NUM_SIMULATION + 1):
    game.initialize_game()
    game.play()
    
x = game.print_game_record()


    
