# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 03:51:46 2020

@author: HP
"""

def binary_adder(num1, num2):
  """
  recieves binary numbers as integer input and returns the sum as an integer
  """
  #first determine the longer bin_number
  max_len = max(len(str(num1)), len(str(num2)))

  #function to convert number to string and also pad up the shorter bin_number with zeros,by appending zero to the front of the number until it becomes equal in length to the longer one
  #this is to ease computation
  def zerofill(num):
    strs = str(num)
    newStr = []
    zeros = max_len - len(strs)
    for i in range(zeros):
      newStr.append('0')  
    newStr.extend(strs)
    return ''.join(newStr)

  x = zerofill(num1)
  y = zerofill(num2)

  #array to store the result of the computation. all initially set to zero
  result = ['0' for _ in range(max_len)]

  #variable to store carry for each computation
  carry = 0

  #iterate through the number(converted to str) from the back i.e in reverse order
  for i in range(max_len-1, -1, -1):
      r = carry
      if x[i] == '1':
        r += 1 
      if y[i] == '1':
        r += 1         
      
      if(int(r%2) == 1):
        result[i] = '1'

      carry = int(r/2)     

  
  #if there is an overflow, which is determined if the value of carry is 1, prepend it to the result
  final_result = str(carry) + (''.join(result))
  return int(final_result)

print(binary_adder(10, 1))
print(binary_adder(10, 10))
print(binary_adder(11, 1))
print(binary_adder(1111111, 1))