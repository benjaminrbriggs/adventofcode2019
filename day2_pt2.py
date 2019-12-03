# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:50:50 2019

@author: Ben
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:59:28 2019

@author: Ben
"""

import pandas as pd

noun = 0
verb = 0
output = 0

while noun <= 99 and output != 19690720:
    verb = 0
    while verb <= 99 and output != 19690720:
        series = pd.read_csv(r'C:\Users\Ben\Documents\AOC\day 2\input.txt', header = None, delimiter = ',')
        
        series[1] = noun
        
        series[2] = verb
        
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
        
        print(verb,noun,output)
        
        verb += 1
        
        
    noun += 1

noun -= 1
verb -= 1
    
print(noun)
print(verb)