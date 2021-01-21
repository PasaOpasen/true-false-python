
import random

def fast_sample(objects, probs):
    """
    returns 1 random object from objects with probs probabilities 
    """
    x = random.random()
    cum = 0
    for i, p in enumerate(probs):
        cum += p
        if x < cum:
            return objects[i]
    return objects[-1]



