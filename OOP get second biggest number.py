# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 00:05:57 2022

@author: Simas Simanavicius

Write a Python program to find the second largest number in Python from the user defined
list.

"""
List_data = [10023, 764556, 7088, 22, 987, 980731, 999]

class Yolo:
    def __init__(self, number):
        self.number = number.sort()
        print(number[-2])

Yolo(List_data)
