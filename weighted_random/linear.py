"""
Linear approach to find a random weighted index
Excerpt from: http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python/
"""

from random import random

def choice(weights):
    """Chooses an index from a list using linear search"""
    totals = []
    running_total = 0

    # calculate weighted list
    for weight in weights:
        running_total += weight
        totals.append(running_total)

    # calculate random number between 0 and the sum of weights
    rnd = random() * running_total

    # find out into which slice rnd falls
    for i, total in enumerate(totals):
        if rnd < total:
            return i
