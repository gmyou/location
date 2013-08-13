# -*- coding:utf-8 -*-

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
    sw1 = float(ne[0])-step
    sw2 = float(ne[1])-step
    s = ne[0] + ',' + ne[1] + '|' + str(sw1) + ',' + str(sw2)
    print s
    

