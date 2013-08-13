# -*- coding:utf-8 -*-

from itertools import product
from sys import float_info
 
_float_min = float_info.min
_epsilon = float_info.epsilon
 
def float_eq(a, b):
    """ floating point comparison from http://floating-point-gui.de/"""
    absA = abs(a)
    absB = abs(b)
    diff = abs(a - b)
    """
    if a == b:
        return True
    elif a == 0 or b == 0 or diff < _float_min:
        return diff < (_epsilon * _float_min)
    else:
        return diff / (absA + absB) < _epsilon
    """
    if a == 0 or b == 0 or diff < _float_min:
        return diff < (_epsilon * _float_min)
    else:
        return diff / (absA + absB) < _epsilon
 
def xxrange(start, stop, step=1):
    cur = start
    while cur < stop:
        yield cur
        cur += step
 
step = 0.1
#lats = xxrange(18.0, 64.0, step)
#lngs = xxrange(-124.0, -66.0, step)

"""
CA
NEÆÀƮ : 41.9,-114.4
SWÆÀƮ : 32.2,-123.9
"""

f = open('grid_ca', 'r')

pos = []

for loc in f:                                                  
    s = loc[1:-2].replace(' ', '')
    ne = s.split(',')
    pos.append(ne)
    
f.close()

for ne in pos:
    sw1 = float(ne[0])-0.1
    sw2 = float(ne[1])-0.1
    s = ne[0] + ',' + ne[1] + '|' + str(sw1) + ',' + str(sw2)
    print s
    

