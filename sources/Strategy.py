# -*- coding: utf-8 -*-
from collections import Counter

"""
from enum import Enum

class Strategy(Enum):
    GREED = greedy_decision
"""  

import random

PLAYER_MEMORY = 7

def update_player_history(history, discard_card):
    history.append(discard_card)
    if len(history) > PLAYER_MEMORY: 
        history.pop(0)
    

def random_decision(hand, history, next_card):
    hand.append(next_card)
    discard_card = discard_random_card(hand)
    hand.remove(discard_card)
    
    update_player_history(history, discard_card)
    return (hand, history, discard_card)

def greedy_decision(hand, history, next_card):
    frequency = Counter(hand)
    wanted_card, wanted_frequency = frequency.most_common(1)[0]
    
    hand.append(next_card)
    discard_card = discard_random_card(hand, wanted_card)
    hand.remove(discard_card)

    update_player_history(history, discard_card)  
    return (hand, history, discard_card)

def greedy_using_history(hand, history, next_card):
    frequency = Counter(hand)
    wanted_card, wanted_frequency = frequency.most_common(1)[0]
    
    if wanted_frequency >= 2:
        return greedy_decision(hand, history, next_card)
    else:
        return greedy_decision(hand, history, next_card)
# =============================================================================
#     fill in later
# =============================================================================
    

def discard_random_card(hand, wanted_card = None):
    hand = hand.copy()
    while wanted_card in hand:
        hand.remove(wanted_card)
    return random.choice(hand)

decision_dictionary = {"GREEDY": greedy_decision,
                       "RAND": random_decision}