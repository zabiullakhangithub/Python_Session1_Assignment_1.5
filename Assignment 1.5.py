# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:34:02 2018

@author: zabiulla.khan

Write a program which accepts a sequence of comma-separated numbers from console
and generate a list.
"""
#option1
# Accept comma seperated numbers
numbers = input("Enter comma seperated numbers:")
#Split the numbers into a list with comma as a seperator
list1 = numbers.split(",")
#print the list
print(list1)
#convert it to a tuple
tuple1 = tuple(list1)
#print  tuple output as well
print(tuple1)

