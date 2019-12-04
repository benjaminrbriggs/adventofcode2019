# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:38:37 2019

@author: Ben
"""

import pandas as pd

series = pd.read_csv(r'C:\Users\Ben\Documents\AOC\day 3\input.txt', header = None, delimiter = ',')

series = series.transpose()

series = series.rename(columns={0:"L1", 1:"L2"})

central_port = pd.DataFrame({"x":[0],"y":[0]})

L1 = pd.DataFrame(central_port,columns = ['x','y'])
L2 = pd.DataFrame(central_port,columns = ['x','y'])

L1 = L1.append(central_port)
L2 = L2.append(central_port)


for row in series.itertuples():
    
    L1_direction = row.L1[:1]
    L1_distance = int(row.L1[1:])

    L2_direction = row.L2[:1]
    L2_distance = int(row.L2[1:])

    L1_temp = 0
    L2_temp = 0
    
    print(row)

    if L1_direction == 'U':               
        while L1_temp < L1_distance:
            L1_temp_df = pd.DataFrame({"x":[L1.iloc[-1]['x']],"y":[L1.iloc[-1]['y']+1]})
            L1 = L1.append(L1_temp_df)
            L1_temp += 1
            print(L1_direction)
            print(row)
            print(L1_temp)
            print(L1_distance)
            
    
    elif L1_direction == 'D':
        while L1_temp < L1_distance:
            L1_temp_df = pd.DataFrame({"x":[L1.iloc[-1]['x']],"y":[L1.iloc[-1]['y']-1]})
            L1 = L1.append(L1_temp_df)
            L1_temp += 1
            print(L1_direction)
            print(row)
            print(L1_temp)
            print(L1_distance)
        
    elif L1_direction == 'L':
        while L1_temp < L1_distance:
            L1_temp_df = pd.DataFrame({"x":[L1.iloc[-1]['x']-1],"y":[L1.iloc[-1]['y']]})
            L1 = L1.append(L1_temp_df)
            L1_temp += 1
            print(L1_direction)
            print(row)
            print(L1_temp)
            print(L1_distance)
            
    elif L1_direction == 'R':
        while L1_temp < L1_distance:
            L1_temp_df = pd.DataFrame({"x":[L1.iloc[-1]['x']+1],"y":[L1.iloc[-1]['y']]})
            L1 = L1.append(L1_temp_df)
            L1_temp += 1
            print(L1_direction)
            print(row)
            print(L1_temp)
            print(L1_distance)
        
            
    if L2_direction == 'U':               
        while L2_temp < L2_distance:
            L2_temp_df = pd.DataFrame({"x":[L2.iloc[-1]['x']],"y":[L2.iloc[-1]['y']+1]})
            L2 = L2.append(L2_temp_df)
            L2_temp += 1
            print(L2_direction)
            print(row)
            print(L2_temp)
            print(L2_distance)
    
    elif L2_direction == 'D':
        while L2_temp < L2_distance:
            L2_temp_df = pd.DataFrame({"x":[L2.iloc[-1]['x']],"y":[L2.iloc[-1]['y']-1]})
            L2 = L2.append(L2_temp_df)
            L2_temp += 1
            print(L2_direction)
            print(row)
            print(L2_temp)
            print(L2_distance)
        
    elif L2_direction == 'L':
        while L2_temp < L2_distance:
            L2_temp_df = pd.DataFrame({"x":[L2.iloc[-1]['x']-1],"y":[L2.iloc[-1]['y']]})
            L2 = L2.append(L2_temp_df)
            L2_temp += 1
            print(L2_direction)
            print(row)
            print(L2_temp)
            print(L2_distance)
            
    elif L2_direction == 'R':
        while L2_temp < L2_distance:
            L2_temp_df = pd.DataFrame({"x":[L2.iloc[-1]['x']+1],"y":[L2.iloc[-1]['y']]})
            L2 = L2.append(L2_temp_df)
            L2_temp += 1
            print(L2_direction)
            print(row)
            print(L2_temp)
            print(L2_distance)
            
intersections_df = L1.merge(L2, how = 'inner', on = ['x','y'])

intersections_df = intersections_df.abs()

intersections_df['distance'] = intersections_df['x'] + intersections_df['y']

intersections_df = intersections_df[intersections_df['distance'] != 0]

print(intersections_df['distance'].min())
