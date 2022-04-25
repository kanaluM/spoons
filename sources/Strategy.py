# -*- coding: utf-8 -*-
from collections import Counter

"""
from enum import Enum

class Strategy(Enum):
    GREED = greedy_decision
"""  

import random

PLAYER_MEMORY = 7

### UPDATE MEMORY ###
def update_player_history(history, card):
    """Adds a card to history list (end) and removes
    first card in list (oldest) if memory limit is exceeded"""
    history.append(card)
    if len(history) > PLAYER_MEMORY: 
        history.pop(0)
    
### STRATEGY HELPER FUNCTIONS ###
def discard_random(hand, history = None, wanted_card = None):
    """Randomly discards any card that is not wanted"""
    return random.choice(hand)

def discard_no_history(hand, history = None, wanted_card = None):
    """Randomly discards any card that is not wanted"""
    discard_candidates = []
    for card in hand:
        if card == wanted_card:
            continue
        discard_candidates += [card]
    return random.choice(discard_candidates)

### POSITIVE MEMORY ###
def discard_history_basic(hand, history, wanted_card = None):
    discard_candidates = []

    # Keep card if wanted or in history
    for card in hand:
        if card == wanted_card:
            continue
        if card in history:
            continue
        discard_candidates += [card]

    # In case no cards are candidates
    if discard_candidates == []:
        return discard_no_history(hand, wanted_card)

    return random.choice(discard_candidates)

def discard_history_random(hand, history, wanted_card = None):
    discard_candidates = []

    # More recent in memory == more likely to keep
    for card in hand:
        if card == wanted_card:
            continue
        if card in history:
            if random.random() < 1/(PLAYER_MEMORY - history.index(card))**0.5:
                continue
        discard_candidates += [card]

    # In case no cards are candidates
    if discard_candidates == []:
        return discard_no_history(hand, wanted_card)

    return random.choice(discard_candidates)

def discard_history_freq(hand, history, wanted_card = None):
    discard_candidates = []
    freq = Counter(history)

    # Keep cards in history that have been seen a lot
    for card in hand:
        if card == wanted_card:
            continue
        if card in history:
            if freq[card] > 1:
                continue
        discard_candidates += [card]

   # In case no cards are candidates
    if discard_candidates == []:
        return discard_no_history(hand, wanted_card)

    return random.choice(discard_candidates)

def discard_history_wild(hand, history, wanted_card = None):
    if random.random() < 0.1:
        return discard_no_history(hand, history = None, wanted_card = wanted_card)
    else:
        return discard_history_basic(hand, history, wanted_card)
    
### NEGATIVE MEMORY ###
def discard_history_basic_N(hand, history, wanted_card = None):
    discard_candidates = []

    # Keep card if wanted or NOT in history
    for card in hand:
        if card == wanted_card:
            continue
        if card not in history:
            continue
        discard_candidates += [card]

    # In case no cards are candidates
    if discard_candidates == []:
        return discard_no_history(hand, wanted_card)

    return random.choice(discard_candidates)

def discard_history_random_N(hand, history, wanted_card = None):
    discard_candidates = []

    # More recent in memory == less likely to keep
    for card in hand:
        if card == wanted_card:
            continue
        if card in history:
            if random.random() > 1/(PLAYER_MEMORY - history.index(card))**0.5:
                continue
        discard_candidates += [card]

    # In case no cards are candidates
    if discard_candidates == []:
        return discard_no_history(hand, wanted_card)

    return random.choice(discard_candidates)

def discard_history_freq_N(hand, history, wanted_card = None):
    discard_candidates = []
    freq = Counter(history)

    # Keep cards in history that have been seen a lot
    for card in hand:
        if card == wanted_card:
            continue
        if card in history:
            if freq[card] == 1:
                continue
        discard_candidates += [card]

   # In case no cards are candidates
    if discard_candidates == []:
        return discard_no_history(hand, wanted_card)

    return random.choice(discard_candidates)

def discard_history_wild_N(hand, history, wanted_card = None):
    if random.random() < 0.1:
        return discard_no_history(hand, history = None, wanted_card = wanted_card)
    else:
        return discard_history_basic_N(hand, history, wanted_card)
    
### MOVE FUNCTION ###
def strat(hand, history, next_card, discard_strat = discard_no_history):
    frequency = Counter(hand)
    wanted_card = frequency.most_common(1)[0][0]
    
    hand.append(next_card)
    discard_card = discard_strat(hand, history, wanted_card)
    hand.remove(discard_card)

    update_player_history(history, discard_card)  
    return (hand, history, discard_card)

decision_dictionary = {"RAND": discard_random,
                       "GREEDY_SIMPLE": discard_no_history,
                       "GREEDY_HIST": discard_history_basic,
                       "GREEDY_HIST_RAND": discard_history_random, 
                       "GREEDY_HIST_FREQ": discard_history_freq,
                       "GREEDY_HIST_WILD": discard_history_wild,
                       "GREEDY_HIST_N": discard_history_basic_N,
                       "GREEDY_HIST_RAND_N": discard_history_random_N, 
                       "GREEDY_HIST_FREQ_N": discard_history_freq_N,
                       "GREEDY_HIST_WILD_N": discard_history_wild_N}