# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 00:41:43 2022

@author: makle

Write a Python program that will Generating a random Strong Password of 15 characters that is a
mixture of upper- & lower-case alphabets, numbers, and special symbols.
Example Output =
Random_strong_password = dTk48@yW&9fsdb£

"""
import string
import random

class Yolo2:
    def __init__(self, length):
        self.length = length
        self.data = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        self.ran = random.sample(self.data,length)
        self.passw = "".join(self.ran)
        return print(self.passw)

Yolo2(15)
