import linear
import binary_search
import subtraction
import king
from preprocessing import WeightedRandomGenerator

if __name__ == "__main__":
    weights = [2, 5, 6, 10]

    print weights

    #print linear.choice(weights)
    #print binary_search.choice(weights)
    #print subtraction.choice(weights)
    #print king.choice(weights)

    generator = WeightedRandomGenerator(weights)
    print generator()
