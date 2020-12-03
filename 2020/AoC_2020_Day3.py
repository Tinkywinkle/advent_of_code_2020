# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:02:51 2020

@author: hamis
"""

# creates a map of '.' and '#' as a list.  Each entry in the list being the 
# equivalent of one line in the map
travelMap = []

file = open("travelMap.txt", "r")

for line in file:
    temp = line.rstrip("\n")
    travelMap.append(temp)
    


def treeEncounter(across, down, grid):
    """ Takes a map of '.' and '#' (grid) and two integers.  Checks the map
    at every interval a certain number of spaces across, and a certain number
    of spaces down.  Returns the number of '#' found over each of these
    intervals."""
    
    line = 0
    column = 0
    trees = 0
    
    # check each line in the map
    for number in range(0, len(travelMap), down):
        # if the length of the counter is greater than the length of line
        # on the map, reet the length of the counter by subtrcting the length
        # of the line
        if line > len(grid[column]) -1:
            line -= len(grid[column])
            
        # if lands on '#', increase the tree counter
        if grid[column][line] == '#':
            trees += 1
        
        column += down
        line = line + across
        
    
    return trees


print("The number of trees hit in question A is:", treeEncounter(3, 1, travelMap))

print("The number of trees hit in question B is:", treeEncounter(1, 1, travelMap)
        * treeEncounter(3, 1, travelMap) * treeEncounter(5, 1, travelMap) * 
        treeEncounter(7, 1, travelMap) * treeEncounter(1, 2, travelMap))