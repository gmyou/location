from itertools import product
from sys import float_info
 
_float_min = float_info.min
_epsilon = float_info.epsilon
 
def float_eq(a, b):
    """ floating point comparison from http://floating-point-gui.de/"""
    absA = abs(a)
    absB = abs(b)
    diff = abs(a - b)
    
    if a == b:
        return True
    elif a == 0 or b == 0 or diff < _float_min:
        return diff < (_epsilon * _float_min)
    else:
        return diff / (absA + absB) < _epsilon
 
def xxrange(start, stop, step=1):
    cur = start
    while cur < stop:
        yield cur
        cur += step
 
step = 0.1
lats = xxrange(18.0, 64.0, step)
lngs = xxrange(-124.0, -66.0, step)
 
locs = reversed([(round(lat, 1), round(lng, 1)) for lat, lng in product(lats, lngs) if not float_eq(lat, lng)])
 
for i, loc in enumerate(locs):                                                  
    print i, loc
