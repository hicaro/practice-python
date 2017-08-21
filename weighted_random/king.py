"""
King of the Hill approach to find a random weighted index
Excerpt from: http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python/

This method does not need to know the amount of weights in advance in order to use it;
So it could be used on some kind of stream
"""

from random import random

def choice(weights):
    """Chooses an index from a list using king of the hill search"""
    total = 0
    winner = 0

    # find out into which slice rnd falls
    for i, weight in enumerate(weights):
        total += weight
        if random() * total < weight:
            winner = i

    return winner
