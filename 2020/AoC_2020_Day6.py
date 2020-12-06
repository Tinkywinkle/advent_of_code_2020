# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:20:26 2020

@author: hamis
"""


def numOfLettersPresent(line):
    """ takes a string and returns the number of letters in the alphabet in
    that string."""
    total = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for letter in alphabet:
                if letter in line:
                    total += 1
    return total

def howManyLettersSame(line):
    """ takes a list of strings and returns the number of identical alphabet
    letters between all the strings."""
    
    total = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    present = True
    
    for letter in alphabet:
        for number in range(0, len(line)):
            if letter not in line[number]:
                present = False
        if present == True:
            total += 1
        present = True
        
    return total
                
            

    
def declarationCountsA(file):
    """takes a file of strings and returns the total number of yes answers
    between each group of declarations.  Does not include duplicates in group."""
    
    declarationFile = open(file, "r")
    
    total = 0
    current = ""
    
    for line in declarationFile:
        if not line.strip():
            total += numOfLettersPresent(current)
            current = ""           
        else:
            line = line.rstrip("\n")
            current += line
            
    # add last line to total (no new line afterwards)    
    total += numOfLettersPresent(current)
    
    return total


def declarationCountsB(file):
    """takes a file of strings, and returns the total number of identical
    yes answers between each group."""
    
    declarationList = []
    declaration = []
    total = 0
    declarationFile = open(file, "r")
    
    for line in declarationFile:
        if not line.strip():
            declarationList.append(declaration)
            declaration = []
        else:
            line = line.rstrip("\n")
            declaration.append(line)
            
    for item in declarationList:
        total += howManyLettersSame(item)
    
    return total
            


          
print("The total number of yes answers for all of the groups is:", 
      declarationCountsA("DeclarationForms.txt"))
print("The total number of yes answers the same for each group is:",
      declarationCountsB("DeclarationForms.txt"))
