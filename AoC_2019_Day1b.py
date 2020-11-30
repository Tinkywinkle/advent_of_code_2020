# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:25:26 2020

@author: hamis
"""

import math

# initialise total amount of fuel needed
total = 0
total_fuel = 0

# open fuel inputs from text file "FuelInput.txt" as read only
mass_input = open("MassInput.txt", "r")

# do some maths on each line and add to total
for line in mass_input:
    mass = int(line)
    while mass > 0:
        mass = (math.floor(mass / 3) - 2)
        if mass > 0:
            total_fuel += mass
    
print(total_fuel)