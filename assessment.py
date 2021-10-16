# Assesment

'''
Write a Python program to sort the numbers in the list (list_values) 
store it in a new created list 
then find the sum of all numbers present in the list. 
Do not forget to Write the algorithm and flowchart for the same.

list_values=[5,8,2,3,11,9,19,1,10,7]
'''
#importing Libraries
import numpy as np

list_values=[5,8,2,3,11,9,19,1,10,7] #given array should be shorted
list_values.sort() #sorting array using NumPy lib
values_sum = np.sum(list_values) #sorting and storing sum of the array using NumPy and saving it to another variable

#additional strings to create desired addition to display with our printed variables to make it readable to end-user
word = "New_sorted_list ="
word2 = "Sum_of_list_values="
#Print result
print(word, list_values) 
print(word2, values_sum)
