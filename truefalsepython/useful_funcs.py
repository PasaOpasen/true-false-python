import sys
import random


def randomTrue(prob = 0.5):
    return True if random.random() < prob else False


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




def set_trace():
    from IPython.core.debugger import Pdb
    Pdb(color_scheme = 'Linux').set_trace(sys._getframe().f_back)


def debug(f, *args, **kwargs):
    from IPython.core.debugger import Pdb
    pdb = Pdb(color_scheme = 'Linux')
    return pdb.runcall(f, *args, **kwargs)
