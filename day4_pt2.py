# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 22:06:36 2019

@author: Ben
"""

x = 152085
last = 670283

password_count = 0

while x <= last:
    found_dupe = False
    asc_dig = True
    x_array = [int(d) for d in str(x)]
               
    for y in range (0,10):
        if str(x).count(str(y)) == 2:
            found_dupe = True

    if found_dupe == True:
        for i in range(0,6):
            for j in range(i+1,6):
                if x_array[j] < x_array[i]:
                    asc_dig = False
    
    if found_dupe == True and asc_dig == True:
        password_count += 1
        print(x)
    x += 1
print(password_count)