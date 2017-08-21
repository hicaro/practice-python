"""
Pre-processing approach to find a random weighted index
Excerpt from: http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python/

Useful when need to make multiple calls using the same weight distribution list
"""

from random import random
from bisect import bisect_right

class WeightedRandomGenerator(object):
    """Chooses an index from a list using generator class"""

    def __init__(self, weights):
        self.totals = []
        running_total = 0

        for weight in weights:
            running_total += weight
            self.totals.append(running_total)

    def next(self):
        """find next random weighted index"""
        rnd = random() * self.totals[-1]
        return bisect_right(self.totals, rnd)

    def __call__(self):
        return self.next()
