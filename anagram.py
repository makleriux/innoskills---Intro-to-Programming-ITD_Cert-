# -*- coding: utf-8 -*-
"""
Created on Mon Nov  15 21:45:53 2021

@author: Simas Simanavicius
Rev.1

Write a Python program that will check whether the two user-defined strings are an anagram or not

Example: string1= ‘plan’
 String2=’nla’
 Output: string1 ‘plan’ and string2 ‘nla’ is not an anagram.
Example 2: string1= 'earth’
 string2=’heart’
 Output: string1 ‘earth’ and string2 ‘hearth’ are an anagram.
"""
# get strings from user
string_1 = input("Enter first string:")
string_2 = input("Enter second string:")
# sort string letters 
sorted_string_1 = sorted(string_1)
sorted_string_2 = sorted(string_2)
# compare letters if they are anagram
if sorted_string_1 == sorted_string_2:
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")        
         
