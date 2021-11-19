# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 16:37:39 2021

@author: Simas Simanavicius
Rev.1

Write a Python program that will check whether the string present in the list (list_of_strings) is palindrome or not. Do 
not forget to Write the algorithm and flowchart for the same.

"""

list_of_strings = ['trap', 'madam', 'hope', 'kayak']
#for every item in list
for i in list_of_strings:
    #reverse string and compare if its polindrome
    if i == i[::-1]:
        print(f'"{i}" is a palindrome word')
    else:
        print(f'"{i}" is not a palindrome word')

'''
Expected Output =
 ‘trap’ is not a palindrome word
 ‘madam’ is a palindrome word
 ‘hope’ is not a palindrome word
 ''kayak’ is a palindrome word
 '''
