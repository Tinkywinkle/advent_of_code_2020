# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:21:25 2020

@author: hamis
"""
seatingChart = []
row = 0
file = open("SeatingChart.txt", "r")

for line in file:
    seatingChart.append([])
    for seat in line:
        seatingChart[row].append(seat.strip())
        if "" in seatingChart[row]:
            seatingChart[row].remove("")
    row += 1

def adjacentSeats(chart, row, column):
    
    seats = []
    
    if column > 0 and column < len(chart[row]) - 1:
        seats.append(chart[row][column + 1])
        seats.append(chart[row][column - 1])
    elif column == 0:
        seats.append(chart[row][column + 1])
    else:
        seats.append(chart[row][column - 1])
        
    if row > 0 and row < len(chart) - 1:
        if column > 0 and column < len(chart[row]) - 1:
            [seats.append(item) for item in chart[row + 1][column - 1:column + 2]]
            [seats.append(item) for item in chart[row - 1][column - 1:column + 2]]
        elif column == 0:
            [seats.append(item) for item in chart[row + 1][column:column + 2]]
            [seats.append(item) for item in chart[row - 1][column:column + 2]]
        else:
            [seats.append(item) for item in chart[row + 1][column - 1:column + 1]]
            [seats.append(item) for item in chart[row - 1][column - 1:column + 1]]
    elif row == 0:
        if column > 0 and column < len(chart[row]) - 1:
            [seats.append(item) for item in chart[row + 1][column - 1:column + 2]]
        elif column == 0:
            [seats.append(item) for item in chart[row + 1][column:column + 2]]
        else:
            [seats.append(item) for item in chart[row + 1][column - 1:column + 1]]
    else:
        if column > 0 and column < len(chart[row]) - 1:
            [seats.append(item) for item in chart[row - 1][column - 1:column + 2]]
        elif column == 0:
            [seats.append(item) for item in chart[row - 1][column:column + 2]]
        else:
            [seats.append(item) for item in chart[row - 1][column - 1:column + 1]]
  
    return seats

    
def filledSeatingChart(chart):
    # create an empty chart to fill
    newChart = []
    for line in range(0, len(chart)):
        newChart.append([])
        for column in range(0, len(chart[line])):
            newChart[line].append("")
    
   
    for rowNumber in range(0, len(chart)):
       for columnNumber in range(0, len(chart[rowNumber])):
           
           if chart[rowNumber][columnNumber] == "L" and "#" not in adjacentSeats(chart, rowNumber, columnNumber):
               newChart[rowNumber][columnNumber] = "#"
           elif chart[rowNumber][columnNumber] == "#" and adjacentSeats(chart, rowNumber, columnNumber).count("#") >= 4:
               newChart[rowNumber][columnNumber] = "L"
           else:
               newChart[rowNumber][columnNumber] = chart[rowNumber][columnNumber]
               
    return newChart

               
def occupiedSeats(chart):
    
    chart1 = chart
    chart2 = []
    seatCount = 0
    loops = 0
    
    while True:
        loops += 1
        chart2 = filledSeatingChart(chart1)
        if chart1 == chart2:
            for row in chart2:
                for column in row:
                    if column == "#":
                        seatCount+= 1
            return seatCount, loops
        
        else:
            chart1 = chart2
    
    
print("The answer to Part A is:", occupiedSeats(seatingChart))