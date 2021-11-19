# -*- coding: utf-8 -*-
"""
Created on Mon Nov  15 22:45:53 2021

@author: Simas Simanavicius
Rev.1

Write a Python program to find the power of a number using recursion.

"""
# get numbers
number=int(input("Enter number: ")) 
number2=number
power =int(input("enter power: "))
#loop till power number eaqual to 1
while 1 < power:
    number2 = number2 * number    
    power = power-1
# print result    
print("Answer is: " + str(number2))

    

    