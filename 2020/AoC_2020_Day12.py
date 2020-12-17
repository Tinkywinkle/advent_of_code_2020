# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 17:16:54 2020

@author: hamis
"""

navigationInstructions = []

file = open("ShipNavigation.txt", "r")

for line in file:
    navigationInstructions.append(line.strip())
    

def shipLocPredict(initialFacing, instructions):
    
    facing = initialFacing
    east = 0
    north = 0
    
    for direction in instructions:
        
        heading = direction[0]
        # change heading to appropriate direction if forward selected
        if heading == "F":
            heading = facing
        # move ship in direction of appropriate heading    
        if heading == "N":
            north += int(direction[1:])
        elif heading == "S":
            north -= int(direction[1:])
        elif heading == "E":
            east += int(direction[1:])
        elif heading == "W":
            east -= int(direction[1:])
        else:
            facing = changeFacing(facing, direction)
            
    return abs(east) + abs(north)


            
def changeFacing(initialFacing, change):
    
    compass = 0
    direction = {"N":0, "E":90, "S":180, "W":270}
    
    compass = direction[initialFacing]
    
    if change[0] == "R":
        compass += int(change[1:])
    elif change[0] == "L":
        compass -= int(change[1:])
    
    while compass < 0 or compass >= 360:
        if compass < 0:
            compass += 360
        if compass >= 360:
            compass -= 360
            
    for key, value in direction.items():
        if value == compass:        
            return key
        
def shipLocPredictionB(initialFacing, instructions):
    
    waypoint = ["E10", "N1"]
    
    east = 0
    north = 0
    
    for direction in instructions:
        if direction[0] == "F":
            east, north = moveShip(waypoint, east, north, int(direction[1:]))
            
        if direction[0] == "N" or direction[0] == "S" or direction[0] == "E" or direction[0] == "W":
            waypoint = waypointChange(waypoint, direction)
            
                    
        if direction[0] == "R" or direction[0] == "L":
            waypoint = changeDirection(waypoint, direction)
    
    return abs(east) + abs(north)

       
            
def moveShip(orders, east, north, multiplier):    
    
    for order in orders:
        if order[0] == "N":
            north += int(order[1:]) * multiplier
        elif order[0] == "S":
            north -= int(order[1:]) * multiplier
        elif order[0] == "E":
            east += int(order[1:]) * multiplier
        elif order[0] == "W":
            east -= int(order[1:]) * multiplier
            
    return east, north
    
def waypointChange(waypoint, change): 
    
    for point in range(0, 2):
        if change[0] == "N"and waypoint[point][0] == "N":
            number = int(waypoint[point][1:]) + int(change[1:])
            waypoint[point] = waypoint[point][0] + str(number)
        if change[0] == "N"and waypoint[point][0] == "S":
            number = int(waypoint[point][1:]) - int(change[1:])
            if number < 0:
                waypoint[point] = "N" + str(abs(number))
            else:
                waypoint[point] = waypoint[point][0] + str(number)
                
        if change[0] == "S"and waypoint[point][0] == "S":
            number = int(waypoint[point][1:]) + int(change[1:])
            waypoint[point] = waypoint[point][0] + str(number)
        if change[0] == "S"and waypoint[point][0] == "N":
            number = int(waypoint[point][1:]) - int(change[1:])
            if number < 0:
                waypoint[point] = "S" + str(abs(number))
            else:
                waypoint[point] = waypoint[point][0] + str(number)
                
                
        if change[0] == "E"and waypoint[point][0] == "E":
            number = int(waypoint[point][1:]) + int(change[1:])
            waypoint[point] = waypoint[point][0] + str(number)
        if change[0] == "E"and waypoint[point][0] == "W":
            number = int(waypoint[point][1:]) - int(change[1:])
            if number < 0:
                waypoint[point] = "E" + str(abs(number))
            else:
                waypoint[point] = waypoint[point][0] + str(number)
                
        if change[0] == "W"and waypoint[point][0] == "W":
            number = int(waypoint[point][1:]) + int(change[1:])
            waypoint[point] = waypoint[point][0] + str(number)
        if change[0] == "W"and waypoint[point][0] == "E":
            number = int(waypoint[point][1:]) - int(change[1:])
            if number < 0:
                waypoint[point] = "W" + str(abs(number))
            else:
                waypoint[point] = waypoint[point][0] + str(number)
        
    return waypoint
    
    
def changeDirection(waypoint, change):
    
    compassPoints = ["N", "E", "S", "W"]    
    changeValue = int(change[1:]) / 90
    print(waypoint)
        
    currentWaypoints = [compassPoints.index(waypoint[0][0]), compassPoints.index(waypoint[1][0])]
    
    if change[0] == "L":
        for item in range(0, 2):
            currentWaypoints[item] -= changeValue
            while currentWaypoints[item] < 0:
                currentWaypoints[item] += 4
            
    if change[0] == "R":
        for item in range(0, 2):
            currentWaypoints[item] += changeValue
            while currentWaypoints[item] > 3:
                currentWaypoints[item] -= 4
                           
    return [(compassPoints[int(currentWaypoints[0])] + waypoint[0][1:]),
            (compassPoints[int(currentWaypoints[1])] + waypoint[1][1:])]
        
        
            
            
    

print("The anser to Part A is:", shipLocPredict("E", navigationInstructions))
print("The anser to Part B is:", shipLocPredictionB("E", navigationInstructions))

