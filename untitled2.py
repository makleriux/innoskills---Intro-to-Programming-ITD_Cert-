# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 11:57:06 2021

@author: La l

"""
#add something into set
em_set = set()
em_set.add(5)
em_set.add(7)
em_set.add(13)
em_set.add(18)
#DEBUG
print("this is set with no changed or duplicated values: " + str(em_set))
#add duplicated value
em_set.add(5)
#DEBUG
print("this is set with changed or duplicated values: " + str(em_set))
#print lenght
print("this is the lenght of the set: " + str(len(em_set)))
#remove value
em_set.remove(7)
#DEBUG
print("this is set with removed value of 7: " + str(em_set))



