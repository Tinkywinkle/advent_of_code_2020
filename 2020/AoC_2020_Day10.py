# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 17:44:51 2020

@author: hamis
"""

adaptors = []

file = open("JoltAdaptors.txt", "r")

for line in file:
    adaptors.append(int(line))
    
sortList = sorted(adaptors)
    
def joltDifference(joltlist):
        
    ones = 1 # to include the charging outlet
    threes = 1 # to include the device
    
    for number in range(0, len(sortList) - 1):
        if joltlist[number + 1] - joltlist[number] == 1:
            ones += 1
        elif joltlist[number + 1] - joltlist[number] == 3:
            threes += 1
        else:
            return False
        
    return ones * threes
    
def adaptorArrangements(joltlist):
       
    last = joltlist[len(joltlist) - 1]
    index = [1] + [0] * last + [0, 0]
    
    for adaptor in joltlist:
        index[adaptor] = index[adaptor-1] + index[adaptor-2] + index[adaptor-3]
        if adaptor == last:
            return index[adaptor]

    
print("The answer to Part A is:", joltDifference(sortList))
print("The answer to Part B is:", adaptorArrangements(sortList))
