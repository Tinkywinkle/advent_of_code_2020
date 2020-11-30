# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:04:18 2020

@author: hamis
"""

import math

# initialise total amount of fuel needed
total = 0

# open fuel inputs from text file "FuelInput.txt" as read only
mass_input = open("MassInput.txt", "r")

# do some maths on each line and add to total
for line in mass_input:
    total += (math.floor(int(line)/3) - 2)
    
print(total)