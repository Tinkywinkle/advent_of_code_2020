# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 17:20:11 2020

@author: hamis
"""

boardingPasses = []

file = open("BoardingPass.txt", "r")

for line in file:
    line = line.rstrip("\n")
    boardingPasses.append(line)
    

def findSeatRow(boardingPass, startRow, endRow):
    """ takes a boarding pass, and 2 ints relating to the start and
    end row numbers of the seats.  Returns the row number of 
    the seat relating to that boarding pass."""
    
    row = 0
    
    if startRow == endRow:
        return int(startRow - 1)
    else:
        row = (endRow - (startRow - 1)) / 2
        if boardingPass[0] == "F":
            return findSeatRow(boardingPass[1:], startRow, endRow - row)
        elif boardingPass[0] == "B":
            return findSeatRow(boardingPass[1:], startRow + row, endRow)
        
def findSeatColumn(boardingPass, startColumn, endColumn):
    """ takes a boarding pass, and 2 ints relating to the start and
    end column numbers of the seats.  Returns the column number of 
    the seat relating to that boarding pass."""
    
    column = 0
    
    if startColumn == endColumn:
        return int(startColumn - 1)
    else:
        column = (endColumn - (startColumn - 1)) / 2
        if boardingPass[7] == "L":
            return findSeatColumn(boardingPass[1:], startColumn, endColumn - column)
        elif boardingPass[7] == "R":
            return findSeatColumn(boardingPass[1:], startColumn + column, endColumn)
        
        
def highestSeatID(boardingPasses):
    """ takes a list of boarding passes and returns the highest seatID on the list."""
    
    result = 0
    highest = 0
    
    for boardingpass in boardingPasses:
        result = (findSeatRow(boardingpass, 1, 128) * 8) + findSeatColumn(boardingpass, 1, 8)
        if result > highest:
            highest = result
            
    return highest

def findMySeat(boardingPasses):
    """ takes a list of boarding passes and returns the seat ID of the first
    available seat"""
    
    result = []
    seatIDs = []
    
    # creat list of all possible available seats
    availableSeats = []
    for rowNumber in range(0, 128):
        for columnNumber in range (0, 8):
            availableSeats.append([rowNumber, columnNumber])
    
    # remove all seats from availableSeats with boarding passes
    # create list of current seatIDs from boarding passes
    for boardingpass in boardingPasses:
        result = [findSeatRow(boardingpass, 1, 128), findSeatColumn(boardingpass, 1, 8)]
        if result in availableSeats:
            seatID = (result[0] * 8) + result[1]
            seatIDs.append(seatID)
            availableSeats.remove(result)
    
    # check all remaining seats to see if there is a seat ID either side and
    # return the first available seat    
    for seat in availableSeats:
        ID = (seat[0] * 8) + seat[1]
        if ID + 1 in seatIDs and ID - 1 in seatIDs:
            return((seat[0] * 8) + seat[1])

    
        
print("The highest seat ID is:", highestSeatID(boardingPasses))
print("Your seat is:", findMySeat(boardingPasses))       