# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 03:54:07 2020

@author: HP
"""

def compressor(numbers):
  numbers_dict = {}

  for ch in numbers:
    if ch.isdigit():
      number = int(ch)
      if number in numbers_dict:
        numbers_dict[number] += 1
      else:
        numbers_dict[number] = 1
  
  return tuple(numbers_dict.items())


print(compressor("fgh5678923456"))
