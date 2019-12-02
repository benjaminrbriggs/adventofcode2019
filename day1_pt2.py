# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:52:43 2019

@author: Ben
"""

import pandas as pd



masses = pd.read_csv(r'C:\Users\Ben\Documents\AOC\day 1\input.txt', header =None, names = ['mass'])
    
masses['fuel'] = (masses['mass']/3) - (masses['mass']%3)/3 - 2
    
total_fuel = masses['fuel'].sum()

for row in masses.itertuples():
    temp_fuel = row.fuel
    
    while temp_fuel > 0:
        temp_fuel = temp_fuel/3 - (temp_fuel%3)/3 - 2
        
        if temp_fuel > 0:
            total_fuel += temp_fuel

print(total_fuel)