# Avalon Test

import random

character_list = {
    0: 'Merlin', # Knows all evil except Mordred
    1: 'Percival', # Knows who Merlin is
    2: 'Loyal Servant of Arthur',
    3: 'Loyal Servant of Arthur',
    4: 'Loyal Servant of Arthur',
    5: 'Loyal Servant of Arthur',
    6: 'Loyal Servant of Arthur',
    7: 'Mordred', # Unknown to Merlin
    8: 'Assassin', # Gets to attempt assassination of Merlin if good guys 'win'
    9: 'Oberon', # Unknown to evil
    10: 'Morgana', # Appears as Merlin to Percival
    11: 'Minion of Mordred',
    12: 'Minion of Mordred',
    13: 'Minion of Mordred'
}

curr_characters = [0, 1, 2, 7, 8]
random.shuffle(curr_characters)

for c in curr_characters:
    print(character_list[c])