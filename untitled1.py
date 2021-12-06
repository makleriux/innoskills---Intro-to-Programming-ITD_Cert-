# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 10:55:38 2021

@author: La l
"""
set1 = set()
set1.add(2)
set1.add(3)
set1.add((13,'d','cool'))
set1.add('q')
set1.add(5)
set1.add(3)
set1.add(8)
set1.add((10, 's', 'tool'))
set1.add('z')
set1.add(True)
print("\nSet after update of above elements: ")
print(set1)
print("Lenght of set is " + str(len(set1)))

set2 = set1
set1.remove(5)
print(set2)