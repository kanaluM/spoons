# -*- coding: utf-8 -*-
import random
from sources.Player import Player
from sources.Decks import Decks
from sources.Game import Game

random.seed(42)
NUM_SIMULATION = 1_000

game = Game()
for n in range(NUM_SIMULATION + 1):
    if n % 50 == 0:
        print(n, game.history)
    game.initialize_game()
    game.play()
    
