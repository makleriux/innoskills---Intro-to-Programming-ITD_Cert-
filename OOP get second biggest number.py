# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 00:05:57 2022

@author: Simas Simanavicius

Write a Python program to find the second largest number in Python from the user defined
list.

"""
List_data = [] 
try:     #while geting integers add them to list
    while True:
        List_data.append(int(input()))
except:
    class Yolo:
        def __init__(self, number):
            self.number = number.sort()
            print(number[-2])

Yolo(List_data)
