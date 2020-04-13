# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 02:24:39 2020

@author: HP
"""

"""
function that takes in a text and the maximum number of characters per line as parameters and returns the wrapped text. 
"""
def wrapper(text, max_num):
  """
  text : the text to be wrapped
  max_num : maximum number of characters
  """

  #list to hold characters of new wrapped text. This is to overcome the overhead of repeated string concatenation during the operation
  new_text = []

  #counter to count current number of characters per line, it is resetted everytime we get to a new line
  counter = 0

  #iterate through the input text, append the characters to the new_text list, when we hit a "new line character" or counter has reached our max_num, then we append a new line character to the new_text list
  for ch in text:
    counter += 1
    new_text.append(ch)
    if(ch == '\n'):
      counter = 0    
    if(counter == max_num):
      new_text.append('\n')
      counter = 0
  
  return ''.join(new_text)


print(wrapper("Hello child sally\nHello madam hopey", 6))