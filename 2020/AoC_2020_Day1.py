# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:28:31 2020

@author: hamis
"""

file = open("ExpenseReport.txt", "r")

# store all numbers in expenses file into a single list
expenses = []

for line in file:
   expenses.append(int(line))


                   
def expenseCalcA():
    """ Take a list of numbers and fine 2 numbers in the list that add to 2020.
    Return the product of those numbers."""
    
    end = len(expenses)
    
    for number1 in range(end):
        for number2 in range(number1 + 1, end):
            if expenses[number1] + expenses[number2] == 2020:
                return expenses[number1] * expenses[number2]
    
    return None

def expenseCalcB():
    """ Take a list of numbers and fine 3 numbers in the list that add to 2020.
    Return the product of those numbers."""
    end = len(expenses)
    
    for number1 in range(end):
        for number2 in range(number1 + 1, end):
            for number3 in range (number2 + 1, end):
                if expenses[number1] + expenses[number2] + expenses[number3] == 2020:
                    return expenses[number1] * expenses[number2] * expenses[number3]
    
    return None


print('The answer to PartA is', expenseCalcA())
print('The answer to PartB is', expenseCalcB())