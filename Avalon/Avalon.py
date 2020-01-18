# Avalon Test

import random

character_list = {
    0: 'Merlin',
    1: 'Percival',
    2: 'Loyal Servant of Arthur',
    3: 'Loyal Servant of Arthur',
    4: 'Loyal Servant of Arthur',
    5: 'Loyal Servant of Arthur',
    6: 'Loyal Servant of Arthur',
    7: 'Mordred',
    8: 'Assassin',
    9: 'Oberon',
    10: 'Morgana',
    11: 'Minion of Mordred',
    12: 'Minion of Mordred',
    13: 'Minion of Mordred'
}

curr_characters = [0, 1, 2, 7, 8]
random.shuffle(curr_characters)

for c in curr_characters:
    print(character_list[c])