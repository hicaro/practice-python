"""
Subtraction approach to find a random weighted index
Excerpt from: http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python/

Using the weight list in descending order increases algorithm speed,
once it removes larger chuncks in the beginning
"""

from random import random

def choice(weights):
    """Chooses an index from a list using total subtraction"""
    # calculate random number between 0 and the sum of weights
    rnd = random() * sum(weights)

    # find out into which slice rnd falls
    for i, weight in enumerate(weights):
        rnd -= weight
        if rnd < 0:
            return i
