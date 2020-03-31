# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 05:20:40 2020

@author: HP
"""

import itertools

#this function takes in a list and return a list containing all possible sublists
#using the principle of combination and the inbuilt function in python for computing combinations in a list
#lst: input list
def power_list(lst):

  #list to store the computed combinations or sublists
  sublists = []

  #for each element in the input lst compute possible sublist and append it to the power_list
  for i in range(len(lst)+1):
      for sublist in itertools.combinations(lst, i):
          sublists.append(sublist)

  return sublists


print(power_list([1, 2, 3, 4, 5]))