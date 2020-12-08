# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:09:12 2020

@author: hamis
"""



instructions = []

file = open("GameInstructions.txt", "r")

for line in file:
    instructions.append(line.split())
    

def findNewPosition(current, change):
    if change[0] == "+":
        return current + int(change[1:])
    elif change[0] == "-":
        return current - int(change[1:])
    
def findInfLoop(instruct):
    
    accumulator = 0
    prevPositions = []
    currentPosition = 0
    
    while currentPosition not in prevPositions:
        prevPositions.append(currentPosition)
        if currentPosition == len(instruct):
            return ("fixed", accumulator)
        if instruct[currentPosition][0] == "jmp":
            currentPosition = findNewPosition(currentPosition, instruct[currentPosition][1])
        elif instruct[currentPosition][0] == "acc":
            accumulator = findNewPosition(accumulator, instruct[currentPosition][1])
            currentPosition += 1
        elif instruct[currentPosition][0] == "nop":
            currentPosition += 1
            
    return ("infinite", accumulator)

def fixProgram(instruct):
    
    for number in range(0, len(instruct)):
        newList = instruct.copy()
        if newList[number][0] == 'jmp':
            newList[number][0] = 'nop'
            test = findInfLoop(newList)
            if test[0] == "fixed":
                return test[1]
            newList[number][0] = 'jmp'
        if newList[number][0] == 'nop':
            newList[number][0] == 'jmp'
            test = findInfLoop(newList)
            if test[0] == "fixed":
                print(number)
                return test[1]
            newList[number][0] == 'nop'
            
            
            

print("Part A", findInfLoop(instructions)[1])
print("Part B", fixProgram(instructions))
    
        