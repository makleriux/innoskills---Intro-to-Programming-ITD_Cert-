# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 16:55:41 2021

@author: Simas Simanavicius
Rev.1

Write a Python program that will Perform the below operations on the dictionary ‘people’:
    1. Add 3 more people to the dictionary ‘people’.
    2. Modify the name of person 1 from Sam to Sammy.
    3. Delete person 2 from the dictionary.
    4. Show all key values pairs from the dictionary using a for loop. Be sure to nicely format the output of the all the key 
value pairs.
    5. Print the names of people whose age >=1

"""
people = {
    1: {'name': 'Sam', 'age': '27', 'sex': 'Male'}, 
    2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}, 
    3: {'name': 'Tom', 'age': '17', 'sex': 'Male'}, 
    4: {'name': 'Alan', 'age': '42', 'sex': 'Male'}, 
    5: {'name': 'Ula', 'age': '16', 'sex': 'Female'}, 
    6: {'name': 'Zoe', 'age': '23', 'sex': 'Female'},}

print(people[2])

