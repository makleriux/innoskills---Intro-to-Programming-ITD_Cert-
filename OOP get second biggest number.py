# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 00:05:57 2022

@author: Simas Simanavicius

Write a Python program to find the second largest number in Python from the user defined
list.

"""
List_data = [] 
print("\nWrite number and press enter.\nTo Finish press enter key or type non integer and press enter key\n")
try:     #while geting integers add them to list
    while True:
        List_data.append(int(input()))
except:
    class Yolo:
        def __init__(self, number):
            self.number = number.sort()
            print(f" Second biggest number is: {number[-2]}")

Yolo(List_data)
