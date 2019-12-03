# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:59:28 2019

@author: Ben
"""

import pandas as pd


series = pd.read_csv(r'C:\Users\Ben\Documents\AOC\day 2\input.txt', header = None, delimiter = ',')

series[1] = 12

series[2] = 2

opcode = 0

while int(series[opcode]) != 99:
    i1 = opcode + 1
    i2 = opcode + 2
    out = opcode + 3
    
    v1 = int(series[i1])
    v2 = int(series[i2])
    output_loc = int(series[out])

    if int(series[opcode]) == 1:
        result = series[v1] + series[v2]
    elif int(series[opcode]) == 2:
        result = series[v1] * series[v2]

    series[output_loc] = result

    opcode += 4
    
output = int(series[0])

print(output)