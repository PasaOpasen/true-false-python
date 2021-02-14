# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:12:46 2021

@author: qtckp
"""

import sys
sys.path.append('..')


from truefalsepython import set_trace, debug



def f(x, y, z):
    
    x = 2*x + y + z
    
    return x + y + z

debug(f, 1, 2, 3)




for i in range(100):
    if i == 50:
        set_trace()




