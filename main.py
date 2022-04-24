# -*- coding: utf-8 -*-
import random
from sources.Player import Player
from sources.Decks import Decks
from sources.Game import Game

random.seed(42)
NUM_SIMULATION = 100

game = Game(["RAND"]*4)
for n in range(NUM_SIMULATION + 1):
    game.initialize_game()
    game.play()
x = game.print_game_record()


    
