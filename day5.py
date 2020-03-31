# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 22:25:39 2020

@author: HP
"""

import math

#This function computes the nth faithful number. Numbers that can be written as the sum of distinct powers of 7.e.g. faithful(22) = 2457 = (7^4)​ + (7^2) ​+ (7^1).

#The principle used is a special type of series where:
#The nth term is F(n) = (7^(log2(n))) + F(n-(2^(log2(n))))

#This can be achieved easily with a recursive function
#n: the nth term to be found in the faithful series
def faithful(n):
  #F(0) = 0
  if(n==0):
    return 0

  #F(1) = (7^0) + F(0)
  if(n==1):
    return 1
  
  #calculating log2(n)
  #N.B: the result is rounded down to nearest whole number to truncate the decimals
  lg = math.floor(math.log2(n))

  #calculating n-(2^(log2(n)))
  diff = n - math.pow(2, lg)

  #calculating F(n) = (7^(lg) + F(diff)
  #where:
  #lg = log2(n)
  #diff = n-(2^(lg))
  #N.B: the result is rounded down to nearest whole number to truncate the decimals
  result = math.floor(math.pow(7, lg)) + faithful(diff)

  return result


print(faithful(22))

