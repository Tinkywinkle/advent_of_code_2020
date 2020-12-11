# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:58:47 2020

@author: hamis
"""
data = []

file = open("XMASData.txt", "r")

for line in file:
    data.append(int(line.strip()))
    

def sumOfTwo(numberList, number):
    
    for integer1 in numberList:
        for integer2 in numberList[1:]:
            if integer1 + integer2 == number:
                return True
            
    return False
    

def inValidNumber(numberList):
    
    count = 0
    result = True
    
    while result != False:
        numericalList = numberList[count:count+25]
        targetNumber = numberList[count+25]
        if sumOfTwo(numericalList, targetNumber) == False:
            return targetNumber
        else:
            count += 1
    
    return None

def smallestLargest(numbers):
    smallest = None
    largest = None
    
    if numbers[0] <= numbers[1]:
        smallest = numbers[0]
        largest = numbers[1]
    else:
        smallest = numbers[1]
        largest = numbers[0]
        
    for number in range(2, len(numbers)):
        if numbers[number] < smallest:
            smallest = numbers[number]
        if numbers[number] > largest:
            largest = numbers[number]
    print(smallest, largest)        
    return smallest + largest

    
def contiguousSet(data, number):
    
    endItem = 1
    while endItem != len(data):
        for item in range(0, len(data) - endItem):
            if sum(data[item:item + endItem + 1]) == number:
                print(sum(data[item:item + endItem + 1]))
                print(endItem)
                print(data[item:item + endItem + 1])
                return smallestLargest(data[item:item + endItem + 1])
        endItem += 1
        
    return None
    
print("The answer to Part A is:", inValidNumber(data))
print(contiguousSet(data, 542529149))
